from threading import Thread, Lock, current_thread
from time import time
from math import floor
try:
    from queue import Queue
except ImportError:
    from Queue import Queue
from time import sleep

def get_current_thread_id():
    if current_thread().name == 'MainThread':
        return 0
    else:
        return current_thread().get_id()

class OmpThread(Thread):
    def __init__(self, my_id, target=None, num_threads=1, args=None):
        super(OmpThread, self).__init__(name=str(my_id), target=target, args=args)
        self.my_id = my_id
        self.num_threads = num_threads

    def get_id(self):
        return self.my_id

    def get_num_threads(self):
        return self.num_threads


def submit(fun, num_threads, args=None):
    if args is None:
        threads = [OmpThread(i, target=fun, num_threads=num_threads, args=()) for i in range(num_threads)]
    else:
        threads = [OmpThread(i, target=fun, num_threads=num_threads, args=args) for i in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


class ForManager:
    def __init__(self, schedule, chunk, num_threads):
        self.lock = Lock()

        self.worker_done = False
        self.start = None
        self.end = None
        self.step = None
        self.count_up = True
        self.total_iterations_remaining = None
        #self.req_lock = Lock()
        self.num_threads = num_threads
        self.chunk = chunk
        self.schedule = schedule if schedule is not None else 'static'
        self.static_iterations_stacks = [Queue() for x in range(num_threads)]
        self.dynamic_or_guided_queue = Queue()

    def setup_worker(self, arg1, arg2, arg3):
        #self.lock.acquire()
        self.start = arg1 if arg2 is not None else 0
        self.end = arg2 if arg2 is not None else arg1
        self.step = arg3 if arg3 is not None else 1

        self.total_iterations_remaining = int((self.end - self.start) / self.step)

        if self.total_iterations_remaining < 0:
            if self.step >= 0:
                raise Exception('invalid for loop arguments [start: {}, end: {}, step: {}'.format(self.start, self.end, self.step))
            self.count_up = False
            self.total_iterations_remaining *= -1

        if self.total_iterations_remaining == 0:
            raise Exception('invalid for loop arguments [start: {}, end: {}, step: {}'.format(self.start, self.end, self.step))

        if self.schedule == 'static':
            self.set_static_iterations_stacks()

        if self.schedule == 'guided' or self.schedule == 'dynamic':
            if self.chunk is None:
                self.chunk = 1
            self.fill_queue()


    def set_static_iterations_stacks(self):
        '''This function divides the work statically among the threads before
            they begin the loop. each item in the list is a stack of work chunks
            with id matching the list index'''
        if self.chunk is None:
            self.chunk = floor(self.total_iterations_remaining / self.num_threads)
            if self.chunk == 0:
                self.chunk = 1

        thread_index = 0

        while self.total_iterations_remaining > 0:
            if self.total_iterations_remaining < self.chunk:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                    self.static_iterations_stacks[thread_index].put((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1
                    self.static_iterations_stacks[thread_index].put((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

            else:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                    self.static_iterations_stacks[thread_index].put((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1
                    self.static_iterations_stacks[thread_index].put((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0
        #self.lock.release()
        self.worker_done = True

    def setup(self, arg1, arg2, arg3):
        Thread(target=self.setup_worker, args=(arg1, arg2, arg3)).start()

    def fill_queue(self):
        while self.total_iterations_remaining > 0:
            if self.schedule == 'dynamic':

                if self.total_iterations_remaining < self.chunk:
                    if self.count_up:
                        start = int(self.end - self.total_iterations_remaining * self.step)
                        end = int(self.end)
                        self.total_iterations_remaining -= int((end - start) / self.step)
                    else:
                        start = int(self.end + self.total_iterations_remaining * self.step)
                        end = int(self.end)
                        self.total_iterations_remaining -= int((end - start) / self.step) * -1

                    '''print('start: ', start)
                    print('end: ', end)
                    print('remaining iters: ', self.total_iterations_remaining)'''
                    self.dynamic_or_guided_queue.put((start, end, self.step if self.count_up else self.step * -1))
                else:
                    if self.count_up:
                        start = int(self.end - self.total_iterations_remaining * self.step)
                        end = int(start + self.chunk * self.step)
                        self.total_iterations_remaining -= int((end - start) / self.step)
                    else:
                        start = int(self.end + self.total_iterations_remaining * self.step)
                        end = int(start + self.chunk * self.step)
                        self.total_iterations_remaining -= int((end - start) / self.step) * -1

                    '''print('start: ', start)
                    print('end: ', end)
                    print('remaining iters: ', self.total_iterations_remaining)'''
                    self.dynamic_or_guided_queue.put((start, end, self.step if self.count_up else self.step * -1))

            elif self.schedule == 'guided':

                # the chunk size cannot go below the specified chunk size if there is one
                chunk = floor(self.total_iterations_remaining / self.num_threads)
                if chunk < self.chunk:
                    chunk = self.chunk

                if self.total_iterations_remaining < chunk:
                    if self.count_up:
                        start = int(self.end - self.total_iterations_remaining * self.step)
                        end = int(self.end)
                        self.total_iterations_remaining -= int((end - start) / self.step)
                    else:
                        start = int(self.end + self.total_iterations_remaining * self.step)
                        end = int(self.end)
                        self.total_iterations_remaining -= int((end - start) / self.step) * -1

                    '''print('start: ', start)
                    print('end: ', end)
                    print('remaining iters: ', self.total_iterations_remaining)'''
                    self.dynamic_or_guided_queue.put((start, end, self.step if self.count_up else self.step * -1))
                else:
                    if self.count_up:
                        start = int(self.end - self.total_iterations_remaining * self.step)
                        end = int(start + chunk * self.step)
                        self.total_iterations_remaining -= int((end - start) / self.step)
                    else:
                        start = int(self.end + self.total_iterations_remaining * self.step)
                        end = int(start + chunk * self.step)
                        self.total_iterations_remaining -= int((end - start) / self.step) * -1

                    '''print('start: ', start)
                    print('end: ', end)
                    print('remaining iters: ', self.total_iterations_remaining)'''
                    self.dynamic_or_guided_queue.put((start, end, self.step if self.count_up else self.step * -1))
        print('done: ', time())
        self.worker_done = True

    def request(self):
        self.lock.acquire()
        if self.schedule == 'static':
            id = get_current_thread_id()
            if self.worker_done and self.static_iterations_stacks[id].empty():
                self.lock.release()
                return 0, 0, 1

            iters = self.static_iterations_stacks[id].get()
            self.lock.release()
            return iters[0], iters[1], iters[2]
        else:
            if self.worker_done and self.dynamic_or_guided_queue.empty():
                self.lock.release()
                return 0, 0, 1

            item = self.dynamic_or_guided_queue.get()
            self.lock.release()
            return item[0], item[1], item[2]

    def done(self):
        #print('\n\n')
        if self.schedule == 'static':
            return self.static_iterations_stacks[get_current_thread_id()].empty()
        #self.req_lock.release()
        return self.dynamic_or_guided_queue.empty()
    '''def request(self):

        self.req_lock.acquire()
        #sleep(1)
        if self.schedule == 'static' or self.schedule is None:
            id = get_current_thread_id()
            if len(self.static_iterations_stacks[id]) == 0:
                self.req_lock.release()
                return 0, 0, 1
            iters = self.static_iterations_stacks[id].pop(0)
            self.req_lock.release()
            return iters[0], iters[1], iters[2]

        if self.schedule == 'dynamic':

            if self.total_iterations_remaining < self.chunk:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1

                print('start: ', start)
                print('end: ', end)
                print('remaining iters: ', self.total_iterations_remaining)
                self.req_lock.release()
                return start, end, self.step if self.count_up else self.step * -1
            else:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1

                print('start: ', start)
                print('end: ', end)
                print('remaining iters: ', self.total_iterations_remaining)
                self.req_lock.release()
                return start, end, self.step if self.count_up else self.step * -1

        if self.schedule == 'guided':

            # the chunk size cannot go below the specified chunk size if there is one
            chunk = floor(self.total_iterations_remaining / self.num_threads)
            if chunk < self.chunk:
                chunk = self.chunk
            print('chunk: ', chunk)


            if self.total_iterations_remaining < chunk:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1

                print('start: ', start)
                print('end: ', end)
                print('remaining iters: ', self.total_iterations_remaining)
                self.req_lock.release()
                return start, end, self.step if self.count_up else self.step * -1
            else:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(start + chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(start + chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1

                print('start: ', start)
                print('end: ', end)
                print('remaining iters: ', self.total_iterations_remaining)
                self.req_lock.release()
                return start, end, self.step if self.count_up else self.step * -1'''






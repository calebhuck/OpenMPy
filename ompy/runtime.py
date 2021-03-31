from threading import Thread, Lock, current_thread
from time import time
from math import floor
#from jarray import array
'''try:
    from queue import Queue
except ImportError:
    from Queue import Queue'''
from collections import deque
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
        self.queue_lock = Lock()
        self.request_lock = Lock()

        self.worker_done = False
        self.start = None
        self.end = None
        self.step = None
        self.count_up = True
        self.total_iterations_remaining = None
        self.num_threads = num_threads
        self.chunk = chunk
        self.schedule = schedule if schedule is not None else 'static'
        self.static_iterations_stacks = [[] for x in range(num_threads)]
        self.dynamic_or_guided_queue = deque()

    def setup_worker(self, arg1, arg2, arg3):
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
                    self.static_iterations_stacks[thread_index].append((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(self.end)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1
                    self.static_iterations_stacks[thread_index].append((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

            else:
                if self.count_up:
                    start = int(self.end - self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step)
                    self.static_iterations_stacks[thread_index].append((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0

                else:
                    start = int(self.end + self.total_iterations_remaining * self.step)
                    end = int(start + self.chunk * self.step)
                    self.total_iterations_remaining -= int((end - start) / self.step) * -1
                    self.static_iterations_stacks[thread_index].append((start, end, self.step))
                    thread_index += 1
                    if thread_index == self.num_threads:
                        thread_index = 0
        #self.lock.release()
        self.worker_done = True

    def setup(self, arg1, arg2, arg3):
        Thread(target=self.setup_worker, args=(arg1, arg2, arg3)).start()

    def fill_queue(self):
        #self.lock.acquire()
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
                    #self.queue_lock.acquire()
                    self.dynamic_or_guided_queue.append((start, end, self.step if self.count_up else self.step * -1))
                    #self.queue_lock.release()
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
                    #self.queue_lock.acquire()
                    self.dynamic_or_guided_queue.append((start, end, self.step if self.count_up else self.step * -1))
                    #self.queue_lock.release()

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
                    self.dynamic_or_guided_queue.append((start, end, self.step if self.count_up else self.step * -1))
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
                    self.dynamic_or_guided_queue.append((start, end, self.step if self.count_up else self.step * -1))
        print('done: ', time(), ' ', len(self.dynamic_or_guided_queue))
        #self.lock.release()
        self.worker_done = True

    def request(self):
        if self.schedule == 'static':
            id = get_current_thread_id()
            print(self.worker_done, ' ', len(self.static_iterations_stacks[id]))
            if not self.worker_done or not len(self.static_iterations_stacks[id]) == 0:
                while len(self.static_iterations_stacks[id]) == 0:
                    continue
                iters = self.static_iterations_stacks[id].pop(0)
                #self.lock.release()
                print('returning ', iters[0], iters[1], iters[2])
                return iters[0], iters[1], iters[2]
            print('finished')
            #self.lock.release()
            return 0, 0, 1
        else:
            '''#self.request_lock.acquire()
            if self.worker_done and len(self.dynamic_or_guided_queue) == 0:
                self.request_lock.release()
                return 0, 0, 1
            while len(self.dynamic_or_guided_queue) == 0:
                continue
            #self.queue_lock.acquire()
            item = self.dynamic_or_guided_queue.popleft()
            #self.queue_lock.release()
            #print 'thread: ', get_current_thread_id(), item[0], item[1], item[2]
            #self.request_lock.release()
            return item[0], item[1], item[2]'''
            while not self.worker_done:
                continue

            self.queue_lock.acquire()
            if len(self.dynamic_or_guided_queue) == 0:
                self.queue_lock.release()
                return 0, 0, 1

            item = self.dynamic_or_guided_queue.popleft()
            self.queue_lock.release()
            # print 'thread: ', get_current_thread_id(), item[0], item[1], item[2]
            return item[0], item[1], item[2]

    def done(self):
        #print('\n\n')
        if self.schedule == 'static':
            return len(self.static_iterations_stacks[get_current_thread_id()]) == 0
        #self.req_lock.release()
        return len(self.dynamic_or_guided_queue) == 0
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






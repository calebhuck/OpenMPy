import sys
sys.path.append('C:\\Users\Caleb\\PycharmProjects\\OpenMPy\\ompy')
from omp_functions import *
from runtime import *
try:
    from Queue import Queue
except ModuleNotFoundError:
    from queue import Queue
from threading import current_thread
num_threads = 6
schedule = 'static'
chunk = 2
def target_0(comm_q):
    global schedule
    global chunk
    global num_threads
    arg1 = 1
    arg2 = None
    arg3 = None
    for_manager = None
    if get_current_thread_id() == 0:
        for_manager = ForManager(schedule, chunk, num_threads, arg1, arg2, arg3)
        comm_q.put(for_manager)
    else:
        for_manager = comm_q.queue[0]
    while True:
        start, stop, step = for_manager.request()
        for x in range(start, stop, step):
            print('thread: ', omp_get_thread_num(), ' loop iteration: ', x)
            num_threads = 1
            def target_1(comm_q):
                print('nested')
            comm_q = Queue()
            submit(target_1, num_threads, args=(comm_q,))
        if for_manager.done(): break
comm_q = Queue()
submit(target_0, num_threads, args=(comm_q,))
from threading import current_thread

def omp_get_thread_num():
    return current_thread().get_id()

def omp_get_num_threads():
    return current_thread().get_num_threads()
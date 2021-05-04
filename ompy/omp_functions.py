from threading import current_thread

def omp_get_thread_num():
    try:
        return current_thread().get_id()
    except AttributeError:
        # this only happens when called from the main thread
        return 0
def omp_get_num_threads():
    return current_thread().get_num_threads()
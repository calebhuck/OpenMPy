from time import sleep

#pragma omp parallel num_threads(2)
    if omp_get_thread_num() == 0:
        sleep(2)
    #pragma omp barrier
    print('thread: ', omp_get_thread_num())

print('thread: ', omp_get_thread_num())

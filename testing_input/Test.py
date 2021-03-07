
#pragma omp parallel for schedule(dynamic, 3)
    for x in range(18):
        #print('x = ', x)
        print('thread: ', omp_get_thread_num())

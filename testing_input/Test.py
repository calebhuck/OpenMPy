
#pragma omp parallel for num_threads(6) schedule(static, 2)
    for x in range(1):
        #print('x = ', x)
        print('thread: ', omp_get_thread_num(), ' loop iteration: ', x)
        #pragma omp parallel num_threads(1)
            print('nested')
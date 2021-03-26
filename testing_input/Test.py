
#pragma omp parallel for num_threads(4) schedule(static, 5)
    for x in range(20):
        print('hello from thread {}'.format(omp_get_thread_num()))

print('\n\n\n')

#pragma omp parallel num_threads(10)
    print('parallel ', omp_get_thread_num())
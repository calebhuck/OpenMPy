


blah = 3
#pragma omp parallel num_threads(10) reduction(+:blah)
    blah = 1
    sum = 0
    #pragma omp parallel num_threads(2) reduction(+:sum)
        sum = 1
    if omp_get_thread_num() == 0:
        print('first result: ', sum)

print('result: ', blah)




blah = 3
#pragma omp parallel num_threads(10) reduction(max:blah)
    blah = omp_get_thread_num() + 1

print('result: ', blah)

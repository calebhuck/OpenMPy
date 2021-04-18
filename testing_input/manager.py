from time import sleep
sum = 0
#pragma omp parallel num_threads(20) shared(sum)
    for i in range(10):
        sum += 1
print(sum)


#pragma omp parallel num_threads(5)
    if omp_get_thread_num() == 0:
        for i in range(3):
            print('sleeping')
            sleep(2)
    #pragma omp barrier
    print('barrier one')


    if omp_get_thread_num() == 0:
        for i in range(3):
            print('sleeping again')
            sleep(2)
    #pragma omp barrier
    print('barrier two')




blah = 3
#pragma omp parallel for num_threads(10) reduction(+:blah)
    for i in range(10):
        blah += 1

print('result: ', blah)

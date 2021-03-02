
#pragma omp parallel for num_threads(5) schedule(static)
    for x in range(10):
        print('hello from ', x)
        break


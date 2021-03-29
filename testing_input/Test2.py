#pragma omp parallel for num_threads(2) schedule(static)
    for x in range(2):
        print('hello')
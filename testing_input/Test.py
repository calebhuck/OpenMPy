from time import sleep, time
import random
import jarray


num_threads = 12
n = 100000000
arr = jarray.array([1 for x in xrange(n)], 'i')
result = [0 for x in xrange(num_threads)]

t_start = time()
sum = 0
for x in range(len(arr)):
    sum += arr[x]
t_end = time()
serial_time = t_end - t_start
print('serial time: ', serial_time)
print('sum = ', sum)



t_start = time()
#pragma omp parallel for num_threads(3)
    for x in range(len(arr)):
        '''sleep(1)
        print('thread: ', omp_get_thread_num(), ' loop iteration: ', x)'''
        result[omp_get_thread_num()] += 1
sum = 0
for x in result:
    sum += x
t_end = time()

parallel_time = t_end - t_start
print('parallel time: ', parallel_time)
print('sum = ', sum)
print()
print('speedup: ', serial_time/parallel_time)
print('efficiency: ', serial_time/(parallel_time * num_threads))

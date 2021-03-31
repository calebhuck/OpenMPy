from time import sleep, time
import random
import jarray


num_threads = 12
n = 10000000
arr = jarray.array([1 for x in xrange(n)], 'i')
result = jarray.array([0 for x in xrange(num_threads)], 'i')

t_start = time()
s_sum = 0
for x in range(len(arr)):
    s_sum += arr[x]
t_end = time()
serial_time = t_end - t_start
print('serial time: ', serial_time)
print('sum = ', s_sum, '\n\n')



t_start = time()
#pragma omp parallel for num_threads(12) schedule(dynamic)
    for x in range(len(arr)):
        '''sleep(1)
        print('thread: ', omp_get_thread_num(), ' loop iteration: ', x)'''
        result[omp_get_thread_num()] += 1
p_sum = 0
for x in result:
    p_sum += x
t_end = time()
print('end: ', t_end)

parallel_time = t_end - t_start

print('parallel time: ', parallel_time)
print('sum = ', p_sum)
print('speedup: ', serial_time/parallel_time)
print('efficiency: ', serial_time/(parallel_time * num_threads))
print(p_sum == s_sum)

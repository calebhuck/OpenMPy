import sys
import jarray
from time import time
from ompy.omp import *
import csv
from datetime import datetime

if __name__ == '__main__':

    n_range = range(100, 10000000, 500000)
    thread_list = [1, 2, 4, 8]
    result_dir = 'benchmark_results/'
    file_name = result_dir + datetime.now().strftime("%Y_%m_%d-%I_%M") + '__mac__sum__.csv'

    n_vals_row = list(n_range)[:]
    n_vals_row.insert(0, None)

    with open(file_name, 'wb') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(n_vals_row)

    _runtime = []

    for num_threads in thread_list:
        row = []
        row.append(num_threads)
        for n in n_range:

            arr = jarray.array([], int)

            s_sum = 0
            p_sum = 0

            for i in range(n):
                arr.append(1)

            s_start = time()
            for i in range(n):
                s_sum += arr[i]
            s_end = time()
            serial_time = s_end - s_start

            p_start = time()
            #omp parallel num_threads(num_threads) reduction(+:p_sum)
                #omp for schedule(static)
                    for x in range(len(arr)):
                        p_sum += arr[x]
            p_end = time()
            parallel_time = p_end - p_start

            if s_sum != p_sum:
                raise Exception('results don\'t match!')


            if num_threads == 1:
                row.append(serial_time)
            else:
                row.append(parallel_time)
            print('finished: ', num_threads, ' threads ', ' and n = ', n)
        _runtime.append(row)
        with open(file_name, 'ab') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row)

    speedup_row = []
    with open(file_name, 'ab') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([])
        writer.writerow(n_vals_row)
        for i, val in enumerate(thread_list):
            if val == 1:
                continue
            speedup_row.append(val)
            for x in range(1, len(n_range) + 1):
                speedup_row.append(_runtime[0][x] / _runtime[i][x])
            writer.writerow(speedup_row)
            speedup_row = []

        #efficiency
        efficiency_row = []
        writer.writerow([])
        writer.writerow(n_vals_row)
        for i, val in enumerate(thread_list):
            if val == 1:
                continue
            efficiency_row.append(val)
            for x in range(1, len(n_range) + 1):
                efficiency_row.append(_runtime[0][x] / (_runtime[i][x] * val))
            writer.writerow(efficiency_row)
            efficiency_row = []
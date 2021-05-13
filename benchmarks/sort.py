import sys
import jarray
from time import time
from ompy.omp import *
import csv
from datetime import datetime
from random import randint

if __name__ == '__main__':

    n_range = range(5, 700, 2)
    thread_list = [1]
    result_dir = 'benchmark_results/'
    file_name = result_dir + datetime.now().strftime("%Y_%m_%d-%I_%M") + '__mac__sort__.csv'

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

            arr_1 = jarray.array([], int)
            arr_2 = jarray.array([], int)

            for i in range(n):
                arr_1.append(randint(0, 10000))
            arr_2 = arr_1[:]

            if True: #num_threads == 1:
                s_start = time()
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if arr_1[j] > arr_1[j + 1]:
                            arr_1[j], arr_1[j + 1] = arr_1[j + 1], arr_1[j]
                            swapped = True
                    if not swapped:
                        break

                s_end = time()
                serial_time = s_end - s_start
            else:
                serial_time = 9999999999

            #print('serial: ', serial_time)
            if True:# num_threads != 1:
                p_start = time()

                #omp parallel num_threads(num_threads)
                    #omp for schedule(static)
                        for x in range(n - 1):
                            if x % 2 == 0:
                                for i in range(n//2):
                                    if arr_2[2*i] > arr_2[2 * i + 1]:
                                        arr_2[2*i], arr_2[2 * i + 1] = arr_2[2 * i + 1],  arr_2[2*i]
                            else:
                                for i in range(n//2 - 1):
                                    if arr_2[2*i + 1] > arr_2[2 * i + 2]:
                                        arr_2[2*i + 1], arr_2[2 * i + 2] = arr_2[2 * i + 2],  arr_2[2*i + 1]

                p_end = time()
                parallel_time = p_end - p_start
            else:
                parallel_time = 99999999999
            #print('parallel: ', parallel_time)


            print(arr_1, '\n\n')
            print(arr_2, '\n\n\n\n\n\n')
            if arr_2 != arr_1:
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
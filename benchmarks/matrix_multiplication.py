import sys
import jarray
from time import time
from ompy.omp import *
import csv
from datetime import datetime


def matrix_mult(arr_1, arr_2, result_arr, start, end):
    # multiply two square matrices
    row_sum = 0
    for i in range(start, end):
        for j in range(n):
            for k in range(n):
                row_sum += arr_1[i * n + k] * arr_2[k * n + j]
            result_arr[i * n + j] = row_sum
            row_sum = 0

if __name__ == '__main__':
    debug = False
    num_runs = 20
    n_range = range(10, 505, 10)
    thread_list = [1, 2, 4, 8, 12]
    result_dir = 'benchmark_results/'
    platform = 'mac'
    benchmark = 'matrix_mult'
    file_name = result_dir + datetime.now().strftime("%Y_%m_%d--%I_%M")
    file_name += '__' + platform + '__' + benchmark + '__runs_' + str(num_runs) + '__.csv'

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
            run_results = []
            for run in range(num_runs):

                arr_1 = jarray.array([], float)
                arr_2 = jarray.array([], float)
                p_result_arr = jarray.array([], float)
                s_result_arr = jarray.array([], float)

                serial_time = 9999999999999
                parallel_time = 9999999999999

                for i in range(n*n):
                    arr_1.append(float(i))

                for i in range(n*n):
                    arr_2.append(float(i))

                for i in range(n*n):
                    p_result_arr.append(0.0)
                    s_result_arr.append(0.0)

                if debug or num_threads == 1:
                    s_start = time()
                    matrix_mult(arr_1, arr_2, s_result_arr, 0, n)
                    s_end = time()
                    serial_time = s_end - s_start

                if debug or num_threads > 1:
                    p_start = time()
                    #omp parallel num_threads(num_threads)
                        chunk = int(n / num_threads)
                        id = omp_get_thread_num()
                        my_start = id * chunk
                        my_end = my_start + chunk if id < num_threads - 1 else n
                        matrix_mult(arr_1, arr_2, p_result_arr, my_start, my_end)

                    p_end = time()
                    parallel_time = p_end - p_start

                if debug:
                    if s_result_arr != p_result_arr:
                        raise Exception('results don\'t match!')

                if num_threads == 1:
                    run_results.append(serial_time)
                else:
                    run_results.append(parallel_time)

            avg = 0
            for result_index in range(num_runs):
                avg += run_results[result_index]
            avg = avg / num_runs

            row.append(avg)
            print('finished: ', num_threads, ' threads ', ' n = ', n, ' avg time = ', avg)
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
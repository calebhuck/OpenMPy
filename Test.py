from scipy.interpolate import interp1d
from itertools import count
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import time
import csv

# retrieve the discrete points along the frequency response curve from csv file and plot them
with open('freq_response_points.csv') as file:
    reader = csv.reader(file)
    x = []
    y = []
    first = True
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
    x = [round(num, 2) for num in x]
    y = [round(num, 2) for num in y]

    plt.plot(x, y, 'o')
    plt.axis([0, 15, -2, 2])
    plt.show()
    # create a new set of 1000 evenly spaced x coordinates to plot the interpolated function
    xnew = np.linspace(0, 15, num=1000, endpoint=True)

    # create the interpolated function and plot along
    interpY = interp1d(x, y, kind='quadratic', fill_value='extrapolate')
    plt.plot(xnew, interpY(xnew), 'r-', x, y, 'o')
    plt.show()

with open('simulated_sound_input.csv') as soundfile:
    reader = csv.reader(soundfile)
    timestamps = []
    frequencies = []
    first = True
    for row in reader:
        timestamps.append(int(row[0]))
        frequencies.append(float(row[1]))
    print('Timesteps', timestamps, '\n', 'Corresponding Frequencies', frequencies)

try:
    pass
finally:
    pass
#!/usr/bin/python

import numpy as np

x = np.array([[8, 9, 11, 12],
              [1, 2, 2, 1],
              [2, 8, 9, 9],
              [9, 6, 6, 3],
              [3, 3, 3, 3]])

avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

print("Averages: " + str(avg))
print("Variances: " + str(var))
print("Standar Deviations: " + str(std))
#!/usr/bin/python

import numpy as np

X = np.array([[42,40,41,43,44,43],
              [30,31,29,29,29,30],
              [8,13,31,11,11,9],
              [11,11,12,13,11,12]])

cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

polluted = set(cities[np.nonzero(X > np.average(X))[0]])

print(polluted)
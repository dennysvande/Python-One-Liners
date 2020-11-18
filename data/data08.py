#!/usr/bin/python

import numpy as np

basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

copurchases = np.sum(np.all(basket[:,2:], axis=1)) / basket.shape[0]

print(copurchases)
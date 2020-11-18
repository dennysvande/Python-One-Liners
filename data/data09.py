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

copurchases = [(i,j,np.sum(basket[:,i]+basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)]

print(max(copurchases, key=lambda x: x[2]))
#!/usr/bin/python

import matplotlib.pyplot as plt

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

expected_cycles = cardiac_cycle[1:-2] * 10

plt.plot(expected_cycles)
plt.show()
#!/usr/bin/python

import numpy as np

inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

superstars = inst[inst[:,0].astype(float) > 100, 1]

print(superstars)
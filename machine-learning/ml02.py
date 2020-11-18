#!/usr/bin/python

from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[0, "No"],
              [10, "No"],
              [60, "Yes"],
              [90, "Yes"]])

model = LogisticRegression().fit(X[:,0].reshape(-1,1), X[:,1])

print(model.predict([[2],[12],[13],[40],[90]]))
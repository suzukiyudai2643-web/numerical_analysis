# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 02:14:34 2026

@author: suzuk
"""
import numpy as np

def newton_coefficients(x, y):
    x = np.asarray(x, dtype=float)
    a = np.asarray(y, dtype=float).copy()
    for order in range(1, len(x)):
        for i in range(len(x) - 1, order - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - order])
    return a

def newton_evaluate(x_nodes, a, x):
    value = a[-1]
    for k in range(len(a) - 2, -1, -1):
        value = a[k] + (x - x_nodes[k]) * value
    return value


x_nodes=np.array([0, 1, 2, 4, 5, 7])
y_nodes=([1, 0, 13, 249, 616, 2388])

a=newton_coefficients(x_nodes,y_nodes)

print("newton_coefficients:",a)


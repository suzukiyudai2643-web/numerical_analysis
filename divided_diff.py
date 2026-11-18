#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ngoma
"""
# Newton divided difference 
# and evaluation by nested multiplication
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

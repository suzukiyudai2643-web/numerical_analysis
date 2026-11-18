# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:15:15 2026

@author: suzuk
"""


import numpy as np
from Chebyshev_nodes import Chebyshev

from divided_diff import newton_coefficients,newton_evaluate


def f(x):
    return np.sin(x)


x_nodes=Chebyshev(2, 8, 2)

y_nodes=f(x_nodes)

a=newton_coefficients(x_nodes, y_nodes)

value=newton_evaluate(x_nodes, a, 2)

print(x_nodes)

print(y_nodes)

print(value)


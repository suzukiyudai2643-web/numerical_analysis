# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:14:41 2026

@author: suzuk
"""

#%% Chebyshev nodes ex2

import matplotlib.pyplot as plt

import numpy as np

from divided_diff import newton_coefficients,newton_evaluate

from Chebyshev_nodes import Chebyshev

def f(x):
    return np.sin(x)

x_nodes=Chebyshev(-5, 8, 40)


y_nodes=f(x_nodes)

a=newton_coefficients(x_nodes, y_nodes)

value=newton_evaluate(x_nodes, a, 0)

print(a)


print(value)

#%%

x=[0,1,2,4,5,7]

y=[1,0,13,249,616,2388]

a=newton_coefficients(x, y)

value=newton_evaluate(x, a, 3)

value0=newton_evaluate(x, a, 0)

value1=newton_evaluate(x, a, 1)

value2=newton_evaluate(x, a, 2)

value3=newton_evaluate(x, a, 4)

value4=newton_evaluate(x, a, 5)

value5=newton_evaluate(x, a, 7)


print(value0,value1,value2,value3,value4,value5)


print(a)

print(value)










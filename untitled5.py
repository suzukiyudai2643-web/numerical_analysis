# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:14:41 2026

@author: suzuk
"""

#%% Chebyshev nodes ex2

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
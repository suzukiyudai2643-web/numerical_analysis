# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 02:14:34 2026

@author: suzuk
"""
import numpy as np

from divided_diff import newton_coefficients, newton_evaluate


x_nodes=np.array([0, 1, 2, 4, 5, 7])
y_nodes=np.array([1, 0, 13, 249, 616, 2388])

a=newton_coefficients(x_nodes,y_nodes)

print("newton_coefficients:",a)

p3=newton_evaluate(x_nodes, a, 3)

print("newton_evaluate at q=3:",p3)

p5=newton_evaluate(x_nodes, a, 6)

print("newton_evaluate at q=6:",p5)


pj=newton_evaluate(x_nodes, a, x_nodes)
print("newton_evaluate at x_", pj)


# newton_coefficients: [ 1. -1.  7.  7.  1.  0.]
# newton_evaluate at q=3: 76.0
# newton_evaluate at q=6: 1285.0
# newton_evaluate at x_ [1.000e+00 0.000e+00 1.300e+01 2.490e+02 6.160e+02 2.388e+03]


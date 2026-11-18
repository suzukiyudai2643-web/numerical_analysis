# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:09:23 2026

@author: suzuk
"""

import numpy as np

from divided_diff import newton_coefficients,newton_evaluate



def f(x):
    return np.cos(np.pi*x)

def chebyshev(n,xdata):
    for k in range(n+1):
        xdata[k] = np.cos((np.pi*(2*k+1)/(2*(n_4+1))))
        return xdata[k]
    




#%% Degree 4 interpolant at equidistant points :
n_4=4
xdata4 = np.zeros((n_4+1,1))
for k in range((n_4+1)):
    xdata4[k] = np.cos((np.pi*(2*k+1)/(2*(n_4+1)))) #Chebyshev points
ydata4 = np.cos(np.pi*xdata4**2) # Data points
c4 = newton_coefficients(xdata4 ,ydata4) # The coefficents of the interpolant
x = np.linspace(-1,1,100) # The points where to evaluate the interpolant
p4 = newton_evaluate(xdata4,c4,x) # The interpolating polynomial evaluated at x.


print(c4)
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:19:42 2026

@author: suzuk
"""

import numpy as np

import matplotlib.pyplot as plt

from divided_diff import newton_coefficients,newton_evaluate


def f(x):
    return 1/(1+25*x**2)

n=10

a,b=-2,2

nodes_ch=np.zeros(n+1)
t=np.zeros(n+1)

for k in range(n+1):
    t[k]=np.cos((2*k+1)*np.pi/(2*(n+1)))
    nodes_ch[k]=(a+b)/2+(b-a)*t[k]/2

nodes_eq=np.linspace(a, b, n+1)

print(nodes_ch)

print(nodes_eq)



a_ch=newton_coefficients(nodes_ch, f(nodes_ch))


a_eq=newton_coefficients(nodes_eq, f(nodes_eq))


print(a_ch)

print(a_eq)



x=np.linspace(-2,2,500)

y_ch=newton_evaluate(nodes_ch, a_ch, x)

y_eq=newton_evaluate(nodes_eq, a_eq, x)




plt.plot(x,y_ch,'r')

plt.plot(x,y_eq,'b')

plt.plot(x,f(x),'g')

# plt.plot(x,np.abs(y_ch-f(x)),'r')

# plt.plot(x,np.abs(y_eq-f(x)),'b')



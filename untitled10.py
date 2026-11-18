# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:31:23 2026

@author: suzuk
"""

import matplotlib.pyplot as plt

import numpy as np

from divided_diff import newton_coefficients,newton_evaluate

def f(x):
    return(1/(1+25*x**2))

a,b=-5,5

n=15

chev_xnodes=np.zeros(n+1)

t=np.zeros(n+1)

for k in range(n+1):
    t[k]=np.cos((2*k+1)*np.pi/(2*(n+1)))
    chev_xnodes[k]=(a+b)/2+(b-a)*t[k]/2
    
    
eq_xnodes=np.linspace(a,b,n+1)

a_ch=newton_coefficients(chev_xnodes, f(chev_xnodes))

a_eq=newton_coefficients(eq_xnodes, f(eq_xnodes))

x=np.linspace(a,b,500)

y_ch=newton_evaluate(chev_xnodes, a_ch, x)

y_eq=newton_evaluate(eq_xnodes, a_eq, x)



plt.plot(x,f(x),'g')
plt.plot(x,y_ch,'r')
plt.plot(x,y_eq,'b')

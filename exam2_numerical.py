# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:59:53 2026

@author: suzuk
"""

import matplotlib.pyplot as plt

import numpy as np

from divided_diff import newton_coefficients, newton_evaluate

def f(x):
    return(np.exp(-15*x**2))

a,b=-1,1

# 25 points, n=25-1=24


x_eq=np.linspace(a,b,26)

# calculate the coefficients
a_eq=newton_coefficients(x_eq, f(x_eq))


print('P(x)=')
for k in range(1,26):
    if k<25:   
        print(a_eq[k],'*x^',(k-1),'+')
    else :
        print(a_eq[k],'*x^',(k-1))


x=np.linspace(-1,1,500)

plt.plot(x,newton_evaluate(x_eq, a_eq, x),'r')

plt.plot(x,f(x),'g')

#we can see large error as x value goes close to the edge of the interval. 
#So the Runge warning is evident from this.

#%%
n=26

x_ch=np.zeros(26)

t=np.zeros(n)

for k in range(26):
    x_ch[k]=np.cos((2*k+1)*np.pi/(2*(26+1)))

a_ch=newton_coefficients(x_ch, f(x_ch))

print('Q(x)=')

for k in range(1,26):
    if k<25:   
        print(a_ch[k],'*x^',(k-1),'+')
    else :
        print(a_ch[k],'*x^',(k-1))

plt.plot(x,f(x),'g')

plt.plot(x,newton_evaluate(x_ch, a_ch, x),'b')

# It is fixed. As we can see in the graph, two graphs are almost the same.





# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:37:11 2026

@author: suzuk
"""

import numpy as np


a=-100

b=100

def composite_midpoint(f, a, b, N):
    h = (b-a)/(N)
    total = 0
    for j in range(1,N+1):
        midpoint=a+(j-1/2)*h
        total = total+f(midpoint)
    return total*h
    
# def f(x):
#     return x**2
def f(x):
    return np.exp(-x**2)
    


area=composite_midpoint(f, a, b, 1000)

print(area)


def trapezoid(f, a, b, N):
    h=(b-a)/N
    total=0
    xN=b
    for j in range(1,N):
        x=a+j*h
        total += (f(x))
    
    total=2*total+f(a)+f(xN)
    return (h/2)*total


area_tra=trapezoid(f, a, b, 1000)

print('area calculated with trapezoid=',area_tra)


print(np.sqrt(np.pi))








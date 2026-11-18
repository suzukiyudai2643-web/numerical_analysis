# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:50:08 2026

@author: suzuk
"""

import math as m

import numpy as np

from mid_point_rule import composite_midpoint



def comp_simp(f,a,b,N):
    
    if N%2!=0 or N<=0:
        raise ValueError('N must be positive even integer')
    
    fx0=f(a)
    
    fxN=f(b)
    
    sub_interval=(b-a)/N
    
    sum_odd=0
    
    for j in range(1,N//2+1):
        sum_odd += f(a+(2*j-1)*sub_interval)
        
        
    sum_odd=4*sum_odd
    
    sum_even=0
    
    for j in range(1,N//2):
        sum_even += f(a+2*j*sub_interval)
        
    sum_even = 2*sum_even
    
    sum_all=fx0+fxN+sum_odd+sum_even
    
    S_N=sub_interval/3*sum_all
    
    return(S_N)

def f(x):
    
    return(1/(1+x**2))


S_N=comp_simp(f,0,1,20)

m_N=composite_midpoint(f, 0, 1, 20)


print(m_N)

print(S_N)

print(np.pi/4-m_N)

print(np.pi/4-S_N)


    


def g(x):
    return((np.sin(x))**2)


N_sin=comp_simp(g, 0, np.pi, 6)

print(N_sin)

print(f'error by simp,{np.pi/2-N_sin:.3e}')
    
    
    
    
    
    
    
    
    
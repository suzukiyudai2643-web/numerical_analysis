# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:09:21 2026

@author: suzuk
"""

import numpy as np

def Chebyshev(a,b,n):
    x_data=np.zeros(n+1)
    for k in range(n+1):
        t=np.cos((2*k+1)*np.pi/(2*(n+1)))
        x_data[k]=(a+b)/2+(b-a)*t/2
    return x_data


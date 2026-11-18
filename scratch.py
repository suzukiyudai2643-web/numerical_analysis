# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:32:19 2026

@author: suzuk
"""


import numpy as np
import math as m

sum=0

for k in range(4,7):
    sum+= (0.5276**k)*((1-0.5276)**(6-k))*m.comb(6,k)
    
print(sum)

sume=0

for i in range(13):
    sume+=np.exp(-28)*28**i/m.factorial(i)
    
print(1-sume)
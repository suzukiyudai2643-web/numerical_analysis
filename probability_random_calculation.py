# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:44:29 2026

@author: suzuk
"""

import numpy as np

import math as m

print((np.exp(-4))*13)


sum1=0

for i in range(3):
    sum1 += m.comb(200,i)*0.02**i*0.98**(200-i)
    
print(sum1)

print(np.sqrt(300*0.0228*0.9772))

print((7.5-6.84)/2.585)


sum2=0
for k in range(8):
    sum2 += m.comb(300,k)*.0228**k*(1-.0228)**(300-k)
    
print(1-sum2)

sum3=0

for k in range(2):
    sum3 += m.comb(20,k)*.01**k*.99**(20-k)
    
    
print(1-sum3)

sum4=0

for i in range(9):
    sum4 += m.comb(500,i)*0.01**i*0.99**(500-i)
    
print(1-sum4)

print(676/700)
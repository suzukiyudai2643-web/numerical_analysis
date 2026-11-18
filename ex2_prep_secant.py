# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:42:05 2026

@author: suzuk
"""

import numpy as np

def f(x):
    return x**3+x-1

x0,x1=0,1

tol=10**(-15)

denom_tol=10**(-20)

max_iter=200

for k in range(1,max_iter+1):
    if np.abs(f(x1)-f(x0))<=denom_tol:   
        print(x1,k-1,np.abs(x1-x0),np.abs(f(x1)))
        print('denominator is too small')
        break
    x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    x0,x1=x1,x2
    step=np.abs(x1-x0)
    print(x1,k-1,np.abs(x1-x0),np.abs(f(x1)))
    print('\n')
    if step<=tol*(1+np.abs(x1)) and np.abs(f(x1))<=tol:
        print('converged')
        break
    if k==max_iter+1:
        print('did not converge')
        break
        

        
            
    
    
    
    


    
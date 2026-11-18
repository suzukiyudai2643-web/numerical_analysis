# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:36:09 2026

@author: suzuk
"""


## MATH 345 final project

#%% divided diff

import numpy as np

def newton_coefficients(x, y):
    x = np.asarray(x, dtype=float)
    a = np.asarray(y, dtype=float).copy()
    for order in range(1, len(x)):
        for i in range(len(x) - 1, order - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - order])
    return a

def newton_evaluate(x_nodes, a, x):
    value = a[-1]
    for k in range(len(a) - 2, -1, -1):
        value = a[k] + (x - x_nodes[k]) * value
    return value
#%% Chebyshev 

def Chebyshev(a,b,n):
    x_data=np.zeros(n+1)
    for k in range(n+1):
        t=np.cos((2*k+1)*np.pi/(2*(n+1)))
        x_data[k]=(a+b)/2+(b-a)*t/2
    return x_data

#%% define f(a) and f'(a)

import math as m
import matplotlib.pyplot as plt


# from the equation 2asing(50/a)=110, by subtracting 110 from both side,
# obtain function of a which equal to 0

def fa(a):
    return 2*a*np.sinh(50/a)-110
def ga(a):
    return 2*(np.sinh(50/a)-50/a*np.cosh(50/a))

#%% See f(60) and f(70) have different sign
print('f(60)=',fa(60))

print('f(70)=',fa(70))    
# first guess for a, a1=60, a2=70

# f(60)= 1.9826609431448077
# f(70)= -1.277021250356782

# f(60)>0, f(70)<0, by intermediate value theorem
# there exists at least one opint c in (60,70), f(c)=0

# also, for all a>0, f'(a)<0, so the function is only decreasing. This leads to the uniqueness.

#%% bisection method function

# begin with a0=60, a1=70


def bisection(f, a0, a1, tol=1.0e-8, max_iter=200):
    print(f"{'approximation':>18}  {'iteration':>9}  {'error_bound':>18}  {'residual':>18}")

    if f(a0)==0: # verify if a0 is the root
        print('root found at a=', a0, '# of iteration:0, error:0, residual:0')
        return(a0,0,0.0)
    if f(a1)==0: # verify if a1 is the root
        print('root found at a=', a1, '# of iteration:0, error:0, residual:0')
        return(a1,0,0.0)
        
    if f(a0)*f(a1)>0:   # verify if there is a root between a0 and a1, if not, quit
        raise ValueError('bisection condition is not met')
        
    for n in range(1,max_iter):
        c=(a0+a1)/2
        # calculate the mid point
        # stop if the mid point is an exact root
        if f(c)==0:
            print('root found at a=', c, '.# of iteration:', n, '.error:0, residual:0.')
            return(c,n,0.0)
        if f(a0)*f(c)<0:    # if satisfied, there is a root between a0 and c
            a1=c
        
        if f(a1)*f(c)<0:    # if saisfied, there is a root between c and a1
            a0=c    # replace the other end point with the mid point
            
        approximation=(a0+a1)/2
        error_bound=(a1-a0)/2
        residual=f(approximation)
        if error_bound<=tol:
            print('bisection completed at a=', approximation, '.# of iteration:', n, '.error bound:',error_bound, '.residual:',residual,'.')
            return approximation, n, error_bound
        
        print(f"{approximation:>18.12f}  {n:>9}  {error_bound:>18.10g}  {residual:>18.10g}")

#%% Newton's method function       
def Newton_method(f,g,a0, tol=1.0e-8, max_iter=200):
    print(f"{'approximation':>18}  {'iteration':>9}  {'error_estimate':>18}  {'residual':>18}")

    if f(a0)==0:
        print('root found at a=', a0, '# of iteration:0, error:0, residual:0')
        return(a0,0,0.0)
    for n in range(1, max_iter):
        a1 = a0 -f(a0)/g(a0)
        if f(a0)==0:
            print('root found at a=', a1, '# of iteration:', n, 'error:0, residual:0')
        error_estimate=np.abs(f(a1)/g(a1))
        residual=f(a1)
        a0=a1
 
        if error_estimate<=tol:
            print('Newton method completed at a=', a0, '.# of iteration:', n, '.error estimate:',error_estimate, '.residual:',residual,'.')
            return a0, n, error_estimate
        
        print(f"{a0:>18.12f}  {n:>9}  {error_estimate:>18.10g}  {residual:>18.10g}")
        if n == max_iter:
            print('reached max itertion, did not satisfy the tolerance. a=', a0, '.# of iteration:', n, '.error bound:',error_estimate, '.residual:',residual,'.')
        
    return a0, n, error_estimate

#%% approximate the root with bisection method
print('bisection method approximation')
bisection(fa, 60, 70)

#%% approximate the root with Newton's method
# a_0=70  
print('Newton method approximation starting at 70')
a_newton_70=Newton_method(fa,ga, 70)
# a_0=60
print('Newton method approximation starting at 60')
a_newton_60=Newton_method(fa,ga, 60)


# define a as the value we approximated
a=a_newton_60[0]

#%% define f(x) with approximated a
def f(x):
    return a*np.cosh(x/a)-a
#%% actual graph

x=np.linspace(-50,50,200)

plt.figure(1)
plt.plot(x,f(x),'g')

#%% equaly spaced nodes
# let n be the nubmer of nodes
n=11
x_eq=np.linspace(-50,50,n)
y_eq=f(x_eq)

a_eq=newton_coefficients(x_eq, y_eq)

x=np.linspace(-50,50,200)

value_eq=newton_evaluate(x_eq, a_eq, x)

plt.figure(2)
plt.plot(x,value_eq,'r')


#%% Chebyshev nodes
x_ch=Chebyshev(-50, 50, n-1)
y_ch=f(x_ch)

a_ch=newton_coefficients(x_ch, y_ch)

x=np.linspace(-50,50,200)

value_eq=newton_evaluate(x_ch, a_ch, x)

plt.figure(3)
plt.plot(x,value_eq,'b')

#%% plot them in the same figure

plt.figure(4)

plt.plot(x,f(x),'g')

plt.plot(x,value_eq,'r')

plt.plot(x,value_eq,'b')



#%% compute errors for equally spaced nodes

error_eq=0

for k in range(len(x+1)):
    node_error_eq= np.abs(f(x[k])-newton_evaluate(x_eq, a_eq, x[k]))
    error_eq += node_error_eq
    plt.figure(5)
    plt.plot(k,node_error_eq,'bo',markersize=3)
print('error average by equally spaced nodes=', error_eq/len(x))

#%% compute errors for Chebyshev nodes

error_ch=0

for k in range(len(x+1)):
    
    node_error_ch= np.abs(f(x[k])-newton_evaluate(x_ch, a_ch, x[k]))
    error_ch += node_error_ch
    
    plt.figure(5)
    plt.plot(k,node_error_ch,'ro',markersize=3)
    
print('error average by Chebyshev nodes=', error_ch/len(x))


#%% overflow function definition
def u_sub(u):
    return(np.sinh(u)/u-1.1)

def u_sub_derivative(u):
    return((np.cosh(u)*u-np.sinh(u))/u**2)

#%% both function over flows easily
print('50/0.07=',50/0.07)

print('direct evaluation; f(0.07)=',fa(0.07))

print('u subed evaluation; u(714)=',u_sub(714))

#%% approximation by using u sub



approximate_bi=bisection(u_sub, 5/7, 5/6)

approximate_new=Newton_method(u_sub, u_sub_derivative,5/6)

approximate_new=Newton_method(u_sub, u_sub_derivative,5/7)



print('uisng the result from bisection method, a=', 50/approximate_bi[0])

print('using the result from bisection method, error bound=',approximate_bi[2])

print('using the relust from Newton method, a=',50/approximate_new[0])

print('using the result from bisection method, error estimate=',approximate_new[2])




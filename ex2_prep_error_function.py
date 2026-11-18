# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:55:33 2026

@author: suzuk
"""

import numpy as np
import matplotlib.pyplot as plt
from divided_diff import newton_coefficients,newton_evaluate
from Chebyshev_nodes import Chebyshev


def f(x):
    return np.exp(x)*np.sin(x)


x_eqnodes=np.zeros(8+1)

for k in range(8+1):
    x_eqnodes[k]=-8+3/2*k
    
print(x_eqnodes)

y_eqnodes=f(x_eqnodes)

x_chnodes=Chebyshev(-8, 4, 9)

print(x_chnodes)
y_chnodes=f(x_chnodes)


a_eq=newton_coefficients(x_eqnodes, y_eqnodes)

a_ch=newton_coefficients(x_chnodes, y_chnodes)


x_dense=np.linspace(-8,4,5000)


er_eq=np.abs(f(x_dense)-newton_evaluate(x_eqnodes, a_eq, x_dense))


er_ch=np.abs(f(x_dense)-newton_evaluate(x_chnodes, a_ch, x_dense))


# plt.semilogy(x_dense,er_eq,'r','equally spaced')

# plt.semilogy(x_dense,er_ch,'b','Chebyshev erro')



plt.semilogy(x_dense,f(x_dense),'g','actual function')

plt.semilogy(x_dense,newton_evaluate(x_chnodes, a_ch, x_dense),'b','cheby')

plt.semilogy(x_dense,newton_evaluate(x_eqnodes, a_eq, x_dense),'r','equally spaced')

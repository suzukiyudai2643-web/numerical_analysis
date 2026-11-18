# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:26:36 2026

@author: suzuk
"""

from divided_diff import newton_coefficients, newton_evaluate

x=[0,1,2,3,4]

y=[0,1,2,7,2]

a=newton_coefficients(x, y)

print(a)


value=newton_evaluate(x, a, 3)

print(value)

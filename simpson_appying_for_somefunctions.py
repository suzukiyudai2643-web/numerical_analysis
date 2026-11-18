# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:47:02 2026

@author: suzuk
"""

import numpy as np

from composite_simpsons_Rule import comp_simp


deg=10


def f(x) :
    return (x**deg)


a=comp_simp(f, 0, 10, 10)

print(a)

print(1/(deg+1)*10**(deg+1))

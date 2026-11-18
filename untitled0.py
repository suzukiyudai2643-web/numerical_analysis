# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:26:36 2026

@author: suzuk
"""

import numpy as np

print('approximation by mid=',np.exp(1/2)*1/2)

print('error=',1-np.exp(1/2)*1/2)

print('error max=',3*np.exp(1)/24)

print('error min=',np.exp(1)/24)
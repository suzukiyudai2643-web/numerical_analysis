# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:41:49 2026

@author: suzuk
"""

def write_python_file(filename):
    with open(filename) as f:
        data = f.read()
        f.close()
        
    with open("Data.txt", mode="w") as f:
        f.write(data)
        f.close()
        
        
write_python_file("MATH345_final_project.py") #MATH345_final_project.py
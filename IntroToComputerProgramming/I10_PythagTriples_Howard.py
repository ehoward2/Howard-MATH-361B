#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:00:27 2019

@author: emilyhoward
"""

import numpy as np

my_array = np.zeros( [0,4])

for ii in range(1,500):
    for jj in range (ii,500):
        for kk in range (jj,500):
            if ii**2 +jj**2 == kk**2:
                my_array = np.vstack ( [my_array, np.array([ii,jj,kk,ii+jj+kk])])
                

print (my_array[np.where(my_array[:,3]==1026)],'this is the triple we wanted to find.')
print (my_array)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:25:33 2019

@author: emilyhoward
"""


N=100
m=8
multiple_list= []
for i in range(1,N):
    for j in range (1,N):
        if (i*j)%m ==1:
            multiple_list.append(i)
    
   
    
print('Theses are the multiplicative inverses of',m, multiple_list,'there are',len(multiple_list), "multiplicative inverses." )
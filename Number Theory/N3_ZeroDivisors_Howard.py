#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:14:05 2019

@author: emilyhoward
"""


N=100
m=8
zero_list= []
for ii in range(1,N):
    if ii % m == 0:
        zero_list.append(ii)
    
print('Theses are the zero divisors of',m, zero_list,'there are',len(zero_list), "zero divisors." )
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:08:05 2019

@author: emilyhoward
"""
import numpy as np
import math


def primecheck(x):
    if x==1:
        return False
    for ii in range(2,math.floor(np.sqrt(x))+1):
       if x%ii ==0:
           return False
    return True
  


n=5

primelist=[]
for i in range (1,1000):
    if primecheck(i)==True:
        primelist.append(i)
        
print(primelist[n-1], "this is the nth prime number.")
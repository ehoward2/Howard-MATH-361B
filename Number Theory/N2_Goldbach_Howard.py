#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:02:21 2019

@author: emilyhoward
"""

import numpy as np
import math
N= 6000

def primecheck(x):
    if x==1:
        return False
    for ii in range(2,math.floor(np.sqrt(x))+1):
       if x%ii ==0:
           return False
    return True
  
primelist=[]
for i in range (1,6000):
    if primecheck(i)==True:
        primelist.append(i)
 
false = []
for n in range (4,N,2):
    Goldback = False
    for j in range (2,N):
        for p1 in primelist:
            if n>=p1 and n-p1 == j**2:
                Goldback= True
    if Goldback == False:
        false.append (n)
print(false)

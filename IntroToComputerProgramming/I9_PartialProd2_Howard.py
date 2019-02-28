#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:22:43 2019

@author: emilyhoward
"""

import numpy as np

N=1000
List1=[]
Prod1 = 1
a_n = lambda n: 1+ ((n)/(n**4))
for ii in range(1,N):
    Temp=a_n(ii)
    Prod1*=Temp
    List1.append(Prod1)
    
print('The Last 15 Terms of the First Sequence',List1[-15:])

List2=[]
Prod2= 1
b_n = lambda n: 1 + (1.5**n)
for ii in range (1,N):
    Temp=b_n(ii)
    Prod2*=Temp
    List2.append(Prod2)
    
print('The Last 15 Terms of the Second Sequence',List2[-15:])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:46:34 2019

@author: emilyhoward
"""

import numpy as np


N=1000
List1=[]
Sum1 = 0
for ii in range(1,N):
    Temp=(np.log((ii**4)+ii+3))/((np.sqrt(ii))+3)
    Sum1+=Temp
    List1.append(Sum1)
    
print('The First 15 Terms of the First Sequence',List1[:15])
print('The Last 15 Terms of the First Sequence',List1[-15:])


List2=[]
Sum2 = 0
for ii in range (1,N):
    Temp=(np.exp(ii/100)/ii**10)
    Sum2+=Temp
    List2.append(Sum2)
    
print('The First 15 Terms of the Second Sequence', List2[:15])
print('The Last 15 Terms of the Second Sequence',List2[-15:])


List3=[]
Sum3 = 0
for ii in range (1,N):
    Temp=(np.sqrt(ii+3)+7)/(np.log(ii+3))
    Sum3+=Temp
    List3.append(Sum3)
    
print('The First 15 Terms of the Third Sequence', List3[:15])
print('The Last 15 Terms of the Third Sequence',List3[-15:])

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:47:31 2019

@author: emilyhoward
"""

import numpy as np


N=1000
List1=[]
Prod1 = 1
for ii in range(1,N):
    Temp=((ii**3)-1/((ii**3)+1))
    Prod1*=Temp
    List1.append(Prod1)
    
print('The First 15 Terms of the First Sequence',List1[:15])
print('The Last 15 Terms of the First Sequence',List1[-15:])


List2=[]
Prod2= 1
for ii in range (1,N):
    Temp=(np.exp(ii/100)/ii**10)
    Prod2*=Temp
    List2.append(Prod2)
    
print('The First 15 Terms of the Second Sequence', List2[:15])
print('The Last 15 Terms of the Second Sequence',List2[-15:])


List3=[]
Prod3 = 1
for ii in range (1,N):
    Temp=((ii**2)+1/((ii**3)+3))
    Prod3*=Temp
    List3.append(Prod3)
    
print('The First 15 Terms of the Third Sequence', List3[:15])
print('The Last 15 Terms of the Third Sequence',List3[-15:])

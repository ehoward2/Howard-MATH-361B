#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:57:11 2019

@author: emilyhoward
"""
import math
import numpy as np
quad = np.zeros ([0,2])
negativeone = np.zeros ([0,2])
P = 30

def primecheck(x):
    if x==1:
        return False
    for ii in range(2,math.floor(np.sqrt(x))+1):
       if x%ii ==0:
           return False
    return True
primelist=[]
for i in range (1,P+1):
    if primecheck(i)==True:
        primelist.append(i)
        

for p in primelist:
    num = []
    for n in range (0,p):
        for k in range (0,n+1):
            if n==(k**2)%p:
                nn = n in num
                if nn == False:
                    num.append(n)
                kk = k in num
                if kk == False:
                    num.append(k)
    quad = np.vstack ([quad, np.array ([p,len(num)])])

print('These are the  quadractic residues')
print (quad)


for p in primelist:
    Q = "False"
    for n in range (0,p):
        if (p-1) == (n**2)%p:
            Q = "True"
            
    negativeone = np.vstack ([negativeone, np.array([p,Q])])


print ('When -1 is a quadratic residue:')
print (negativeone)
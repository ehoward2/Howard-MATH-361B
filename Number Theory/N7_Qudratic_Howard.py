#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:57:11 2019

@author: emilyhoward
"""
import math
import numpy as np
count = np.zeros ([0,2])
neg_one = np.zeros ([0,2])
P = 50

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
    count = np.vstack ([count, np.array ([p,len(num)])])

print('The quadractic residues are:')
print (count)


for p in primelist:
    QR = "False"
    for n in range (0,p):
        if (p-1) == (n**2)%p:
            QR = "True"
            
    neg_one = np.vstack ([neg_one, np.array([p,QR])])


print ('When -1 is a quadratic residue:')
print (neg_one)
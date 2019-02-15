#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:38:42 2019

@author: emilyhoward
"""

def NNUM (S1, S0):
    for ii in range (2,amount):
        S2=List1[ii-1] + List1[ii-2] 
        List1.append (S2)

            

S0=0
S1=1

amount = 10,000
m = 2
List1=[]
List2 = []

List1.append(S0)
List1.append(S1)
NNUM(S1,S0)

for ii in range (0, amount):
        if List1[ii]%m ==0:
            List2.append(List1[ii])
            
print(List2)
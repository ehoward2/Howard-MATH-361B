#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:34:24 2019

@author: emilyhoward
"""

def divisor (n):
    divisors_list = []
    ii = 1
    while ii < n:
        if (n % ii ==0):
            divisors_list.append(ii)
        ii += 1
    return divisors_list

N= 10000
amicable = []
for a in range (1,N):
    b = sum (divisor(a))
    if sum(divisor(b)) ==a:
        aVal= a in amicable
        if aVal == False:
            amicable.append(a)
        bVal = b in amicable
        if bVal == False:
            amicable.append(b)
            
print("The amicable numbers are:", amicable)
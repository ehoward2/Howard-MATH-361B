#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:15:17 2019

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

my_list = divisor(200)
print(my_list)

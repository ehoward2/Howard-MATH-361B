#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:20:07 2019

@author: emilyhoward
"""

#
N = 50
r_block = BlockFunction(2,N)
g_block = BlockFunction(3,N)
b_block = BlockFunction(4,N)

def BlockFunction(M,N):
    waysofblock = [1] *M + [0]* (N-M +1)
    for ii in range(M,N+1):
        waysofblock[ii] += waysofblock[ii-1] + waysofblock[ii-M]
    return waysofblock[N] - 1



print("Number of Spaces =", N)
print("Number of ways Red fills =",r_block)
print("Number of ways Green fills =",g_block)
print("Number of ways Blue fills =",b_block)
print("Totally number of ways to fill =", r_block+g_block+b_block)


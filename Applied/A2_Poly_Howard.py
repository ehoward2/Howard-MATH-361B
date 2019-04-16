#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:02:40 2019

@author: emilyhoward
"""

P = [2,4,0,-1] #-1x^3+4x+2
G = []
D = []

#def p(x):
#    for i in range (len(P)):
#        l = x **i
#        G.append(P[i]* l)
#    return sum(G)
#    
#print (p(2))

def P_deriv (m):
    for ii in range (len(P)):
        j = ii * P
        D.append (j)
        return D
    for j in range(len(D)):
        k = x**i
        D.append(M[j]*k)
    return D[1:]
        
      
    

print (P_deriv(2))
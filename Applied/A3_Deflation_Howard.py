#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:05:40 2019

@author: emilyhoward
"""
f= [-1,0,0,1]
g= [2,1]
r = list(f)
q = [0]

def r_empty():
    empty = True
    for ii in r:
        if ii != 0:
            empty = False
            break
    return empty


def r_div_g():
    if len(r) >= len(g):
        return True
    else:
        return False
    
def divAddQ(x,y) :
    if len(r) == len(g):
        q.appened(r[-1]/g[-1])
    else:
        for ii in range(0,len(r)-len(g) -1):
            q.insert(ii,0)
        q.insert(len(r)-len(g), r[-1]/g[-1])
    return q

def multigandsub():
    for ii in range(0,len(g)):
        g[ii] = (g[ii]*q[-1])*-1
    for ii in range(0,len(q)-1):
        g.insert(0,0)
    for ii in range (0,len(g)):
        print("at",ii,"r is equal to", r[ii],"+",g[ii])
        r[ii]= r[ii] + g[ii]
    return r

while (r_empty == False) and (r_div_g) == True:
    q = divAddQ(r[-1],g[-1])
    r = multigandsub()
    
"""
q = divAddQ(r[-1],g[-1])
r = multigandsub()
        
"""

print (q)
print (r)
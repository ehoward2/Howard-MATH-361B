#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:38:42 2019

@author: emilyhoward
"""

def nextNum (F1, F0):
    for ii in range (2,term):
        F2=my_list[ii-1] + my_list[ii-2] 
        my_list.append (F2)

            

F0=0
F1=1

term = 10,000
m = 2
my_list=[]
my_list2 = []

my_list.append(F0)
my_list.append(F1)
nextNum(F1,F0)

for ii in range (0, term):
        if my_list[ii]%m ==0:
            my_list2.append(my_list[ii])
            
print(my_list2)
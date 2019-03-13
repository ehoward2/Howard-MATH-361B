#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:04:00 2019

@author: emilyhoward
"""



N= 500
a_0= 70
my_list = [a_0]

for ii in range (1, N):
    if my_list[-1] % 2 == 0:
        my_list.append(my_list[-1]/2)
    elif my_list[-1] == 1:
        break
    else:
        my_list.append(3*my_list[-1]+1)


print (my_list)
print ('It took', len(my_list), 'terms to reach 1')





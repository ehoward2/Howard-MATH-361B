#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:46:34 2019

@author: emilyhoward
"""
import numpy as np

z=3

acumS=np.array([])
for ii in range (0,z):
    np.append(acumS, (np.long(ii**4+ii+3)/np.sqrt(ii)+3))

sumS= np.sum(acumS)

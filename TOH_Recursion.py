#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:10:02 2021

@author: dhruv
"""

def tower(n, sourcePole, destinationPole, auxiliaryPole):
 
    if(0 == n):
        return
 
    tower(n-1, sourcePole, auxiliaryPole, destinationPole)
   
    print("Move the disk from",sourcePole,"to",destinationPole)
  
    tower(n-1, auxiliaryPole, destinationPole,sourcePole)
 
 
tower(3, 'S', 'D', 'A') 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 01:54:37 2021

@author: dhruv
"""

def ladderproblem(n):
    if n==0:
        return 1
    
    if n<0:
        return 0
    
    return ladderproblem(n-1) + ladderproblem(n-2) + ladderproblem(n-3)

ans = ladderproblem(4)
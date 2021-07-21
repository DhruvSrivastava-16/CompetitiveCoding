# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:38:02 2021

@author: DHRUV
"""


def catlannumber(n):
    if n<=1:
        return 1
    
    res = 0
    for i in range(n):
        res += catlannumber(i)*catlannumber(n-i-1)

    return res


n = int(input("enter: "))
ans =  catlannumber(n)

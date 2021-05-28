#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 00:55:17 2021

@author: dhruv
"""

def numstring(num,digits,ans):
    while(num>0):
        print("num",num)
        if num//10 == 0:
            return digits[num]
        
        temp = num%10
        
        return numstring(num//10,digits,ans) + " " + digits[temp]
        

digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
num = 2048

ans = numstring(num,digits,"")

                
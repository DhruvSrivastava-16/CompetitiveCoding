#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 02:32:36 2021

@author: dhruv
"""

def move(n,src,helper,dest):
    if n==0:
        return
    
    move(n-1,src,dest,helper)
    print("shift disk ",n," from ",src," to ",dest," using ",helper)
    move(n-1,helper,src,dest)

n = int(input("Num of disks: "))
move(n,'A','B','C')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:39:47 2021

@author: dhruv
"""

class Node:
    
    def __init__(self,value = 0):
        self.val = value;
        self.next = None;
        
        
root = Node(1)

second = Node(2)
root.next = second

third = Node(3)
second.next = third

t=root

while t:
    print(t.val,end=" ")
    t = t.next
    

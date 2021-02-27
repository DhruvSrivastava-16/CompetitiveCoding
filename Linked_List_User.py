#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:46:39 2021

@author: dhruv
"""

class Node:
    
    def __init__(self,value = 0):
        self.val = value
        self.next = None;
        
n = 0;
root = None
prev=root

while True:
    n = int(input("Enter:"))
    if n == -1:
        break
    
    t = Node(n)
    
    if prev is None:
        root = t;
        prev = t;
    
    else:
        prev.next = t
        prev = prev.next
    
    
    #t.next = Node()
    #t = t.next
    
while root:
     
    print(root.val,end=" *-> ")
     
     
     
    root = root.next

    
    
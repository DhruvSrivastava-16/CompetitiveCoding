#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:30:46 2021

@author: dhruv
"""

class Node:
    
    def __init__(self,key):
        self.key =  key
        self.left = None
        self.right = None 
        
s = set()

def check_duplicate(T):
    if T is None:
        return 
    
    if T.key in s:
        print ("Duplicate Found! and it is:",T.key)
        return 
    
    s.add(T.key)
    
    return check_duplicate(T.left) or check_duplicate(T.right)
        


if __name__ == '__main__':
    
    T = Node(26) 
    T.right = Node(3) 
    T.right.right  = Node(3) 
    T.left = Node(10) 
    T.left.left = Node(4) 
    T.left.left.right = Node(26) 
    T.left.right = Node(6) 
    
    check_duplicate(T)
    
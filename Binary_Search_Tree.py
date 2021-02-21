#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:56:57 2021

@author: dhruv
"""

class BST:
    def __init__(self,key):
        self.right = None;
        self.left = None;
        self.val = key;
        
    def insert(self,data):
        
        if self.val < data:
            if self.right is None: 
                self.right = BST(data)
            
            else: 
                self.insert(data)
                
        elif self.val > data:
            if self.left is None:
                self.left = BST(data)
            
            else:
                self.insert(data)
        
        else:
            self.data = data
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            
        print( self.val),
        
        if self.right:
            self.right.PrintTree()

root = BST(10)
root.insert(11)
root.insert(3)
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:02:38 2021

@author: DHRUV
"""


class treenode:
    
    def __init__(self,val = 0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right
        


root = treenode(1)
l = treenode(2)
r = treenode(3)

root.left = l
root.right = r


print(root,root.val,root.left,root.right)
print(root.left.val, l.val)
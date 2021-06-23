# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:06:36 2021

@author: DHRUV
"""


class treenode:
    
    
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        

def preorder(root):
    if not root:
        return
             
    print(root.val)   
    preorder(root.left)
    preorder(root.right)
    

def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)   
    
def inorder(root):
    if not root:
        return 
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
 
    

root = treenode(8)
n1 = treenode(10)
n2 = treenode(3)

root.left = n1
root.right = n2


n3 = treenode(1)
n4 = treenode(6)
n5 = treenode(14)

n1.left = n3
n1.right = n4
n2.right = n5

n6 = treenode(9)
n4.left = n6
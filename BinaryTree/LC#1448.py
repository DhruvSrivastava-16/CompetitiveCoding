# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:16:43 2021

@author: DHRUV
"""




class treenode:
    
    
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def leafnodes(self,root):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            print(root.val)
            
        self.leafnodes(root.left)
        self.leafnodes(root.right)
        
    def currmax(self,root):   #for finding the max value till discovering node n.
        cm = []
        self.tr(root,cm,root,root.val)
        print(cm)
        return cm
  
    def tr(self,root,cm,mr,tmax = -1):
        if root is None:
            
            return 
        
        
        
        
        if root.val >= tmax:
            tmax = root.val
            
        
        cm.append((root.val,tmax))
        
        
        print (root.val, cm)
            
        
        self.tr(root.left,cm,mr,tmax)
        self.tr(root.right,cm,mr,tmax)
        

        
        
        
        
        
        
        
r = treenode(3)
n1 = treenode(1)
n2 = treenode(4)
n3 = treenode(3)
n4 = treenode(1)
n5 = treenode(5)


r.left = n1
r.right = n2


n1.left = n3
n2.right = n5
n2.left = n4

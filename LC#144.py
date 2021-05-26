#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:38:39 2021

@author: dhruv
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,ans):
        if root:
            ans.append(root.val)
            self.helper(root.left,ans)
            self.helper(root.right,ans)
        return ans 
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = self.helper(root,[])
        return ans
        
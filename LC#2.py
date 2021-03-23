#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:56:31 2021

@author: dhruv
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:         
    def convert_Num(self,l):
        n = 0
        while l:
            n = n*10 + l.val
            l = l.next
            
        x = str(n)
        x = x[::-1]
        x = int(x)
        return(x);
    
    def convert_List(self,n):
        len_n = len(str(n));
        
        root = None;
        prev = root;
        
        while n>1:

            val = n%10;
        
            
            t = ListNode(val)
            
            if prev == None:
                prev = t;
                root = t;
                
                
            else:
                prev.next = t;
                prev = prev.next
                
            
            n = n//10;
        
        return root
        
        
            
            
    def addTwoNumbers(self, l1,l2):
        n1 = self.convert_Num(l1)
        n2 = self.convert_Num(l2)
        print(n1)
        print(n2)
        print("sum: ",n1+n2)
        ans_no = n1+n2;
        if n1 == 0 and n2 == 0 :
            return ListNode()
        ans = self.convert_List(ans_no)
        
       
        
        return ans
        
        
        
s1 = ListNode(9)
a1 = ListNode(9)
b1 = ListNode(9)

        
s2 = ListNode(9)
a2 = ListNode(9)
b2 = ListNode(8)

s1.next = a1
a1.next = b1

s2.next = a2
a2.next = b2

ss = Solution()
n1 = ss.addTwoNumbers(s1,s2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:05:57 2021

@author: dhruv
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        head = tail = ListNode()
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
                
            else:
                tail.next = l2;
                l2 = l2.next
                
            tail = tail.next
            
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        return head.next
        
                
                                
                
            
        

        
                
                
            
            
            
                
            
            
            


s1 = ListNode(1)
a1 = ListNode(2)
b1 = ListNode(4)

        
s2 = ListNode(1)
a2 = ListNode(3)
b2 = ListNode(4)
c2 = ListNode(9)
d2 = ListNode(11)


s1.next = a1
a1.next = b1

s2.next = a2
a2.next = b2
b2.next = c2
c2.next = d2

ss = Solution()
n1 = ss.mergeTwoLists(s1,s2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 22:43:42 2021

@author: dhruv
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        
        fr = dummy;
        bc = dummy;
        
        for i in range(0,n+1):
            fr = fr.next;
            
    
        while fr:
            fr = fr.next
            bc = bc.next
            
        bc.next = bc.next.next
        return dummy.next
        
        
        
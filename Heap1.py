# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:46:57 2021

@author: DHRUV
"""


l  = [ 12, 11, 13, 5, 6, 7]

def maxheapify(i,l):
    left = 2*i + 1
    right = 2*i+ 2
    largest = i
    
    if left < len(l) and l[left] > l[i]:
        largest = left
    
    if right < len(l) and l[right] > l[largest]:
        largest = right
        
    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        maxheapify(largest,l)
        
def buildheap(l):
    s = len(l)
    for i in range(s//2-1,-1,-1):
        maxheapify(i,l)
    
def heapsort(l):
    buildheap(l)
    for i in range(len(l)-1,0,-1):
        l[0], l[i] = l[i], l[0]
    
        maxheapify(0,l)
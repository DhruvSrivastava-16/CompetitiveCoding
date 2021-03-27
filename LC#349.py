#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:24:32 2021

@author: dhruv
"""

def intersection(nums1,nums2):
    
    inter = []
    
    if len(nums1)<len(nums2):
        for i in nums1:
            if i in nums2:
                inter.append(i)
                nums2.remove(i)

                
        
    else:
        for i in nums2:
            if i in nums1:
                inter.append(i)
                nums1.remove(i)
            
    return (inter)

    
if __name__ == '__main__':
    
    nums1 = [1,2,2,1]
    nums2 = [1,1]
    ans = intersection(nums1,nums2)
    
    

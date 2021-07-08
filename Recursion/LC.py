# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:46:48 2021

@author: DHRUV
"""


def ans1(k,bin_ar,num,pos,ans):
    print("K: ",k)
    if k == num:
        print("Found!")
        return
    
    elif k>num:
        t = bin_ar[pos]
        ans.pop()
        ans1(k-t,bin_ar,num,pos-1,ans)
    
    else:
        print(k,bin_ar[pos])
        ans.append(bin_ar[pos])
        ans1(k+bin_ar[pos],bin_ar,num,pos,ans)
        
    

        
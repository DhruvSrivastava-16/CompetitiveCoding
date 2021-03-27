#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 04:39:41 2021

@author: dhruv
"""


def prefixsum(arr):
    nc = len(arr[0])
    nr = len(arr)
    
    for j in range(1,nc):
        arr[0][j] = arr[0][j-1] + arr[0][j]
        
    for i in range(1,nr):
        arr[i][0] = arr[i-1][0] + arr[i][0]
        
    for i in range(1,nr):
        for j in range(1,nc):
            arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + arr[i][j]
            
    print(arr)
            
class NumMatrix:

    def __init__(self, matrix):
        self.m = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        prefixsum(self.m);
        
        print(self.m)    
        
        return self.m[row2][col2] - self.m[row1-1][col2] - self.m[row2][col1-1] + self.m[row1-1][col1-1]
        
        
    # for i in range(0,nr):
    #     for j in range(0,nc):
    #         arr[i][j] = arr[i][j-1] + arr[i][j]
            
    # return 1

arr = [[3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

#[2,1,4,3],[1,1,2,2],[1,2,2,4]]

s = NumMatrix(arr);
ans = s.sumRegion(1, 2, 2, 4)
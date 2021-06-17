# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:18:24 2021

@author: DHRUV
"""



def solution(W,P,N,C):
    
    choosing_ob_prof = 0
    if N ==  0 or C == 0:
        return  0
    
    if W[0] <= C:
        choosing_ob_prof = P[0] + solution(W[1:],P[1:],N-1,C-W[0])
    
    notchoosing_prof = solution(W[1:],P[1:],N-1,C)
    
    return max( choosing_ob_prof,  notchoosing_prof )


W = [1,2,3,5]
P = [40, 20, 30, 100]

N = 4
C = 7

#whats the maximum profit that we can get?

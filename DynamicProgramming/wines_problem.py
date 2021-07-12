# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:05:11 2021

@author: DHRUV
"""


#This is not a DP solution, it is a recursive solution

def rec_sol(wines,st,end,year,tp):
    
    #print("ST: ",st,"End: \n",end)
    
    if st == end:
        return wines[st]*year
    
    left_prof = wines[st] * year + rec_sol(wines,st+1,end,year+1,tp)
    right_prof =  wines[end] * year + rec_sol(wines,st,end-1,year+1,tp)
    
    if left_prof>right_prof:
        print("Beg\n")
    
    else:
        print("End\n")
    
    return tp + max(left_prof,right_prof)
    


def bottom_up_DP(wines,DP,i,j,y):
    if i>j:
        #DP[i][j] = 0
        return 0
        
    if DP[i][j]!=0:
        return DP[i][j]
    
    left = wines[i]*y + bottom_up_DP(wines,DP,i+1,j,y+1)
    right = wines[j]*y + bottom_up_DP(wines,DP,i,j-1,y+1)
    DP[i][j] =  max(left,right)
    
    
    return DP[i][j]





wines = [2,4,6,2,5]

#-------------------------

year = 1
st = 0
end = len(wines) - 1
tp = 0

#-------------------------

y = 1
i = 0
j = len(wines) - 1
DP =  DP = [[0 for i in range(0,len(wines))] for j in range(0,len(wines))]


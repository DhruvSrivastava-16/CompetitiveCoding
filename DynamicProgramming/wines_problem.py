# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:05:11 2021

@author: DHRUV
"""


def dp_sol(wines,st,end,year,tp):
    
    #print("ST: ",st,"End: \n",end)
    
    if st == end:
        return wines[st]*year
    
    left_prof = wines[st] * year + dp_sol(wines,st+1,end,year+1,tp)
    right_prof =  wines[end] * year + dp_sol(wines,st,end-1,year+1,tp)
    
    if left_prof>right_prof:
        print("Beg\n")
    
    else:
        print("End\n")
    
    return tp + max(left_prof,right_prof)
    


wines = [2,4,6,2,5]
year = 1
st = 0
end = len(wines) - 1
tp = 0


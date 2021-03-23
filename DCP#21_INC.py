#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:25:27 2021

@author: dhruv
"""

schedule = [(4, 10), (5, 44), (88, 99) , (1,6)];
schedule = sorted(schedule,key = lambda x :x[1])
classes = 0;
j = 1

for i in range(0,len(schedule) - 1):
    
    temp = [x for x in range(schedule[i][0],schedule[i][1]+1)]
    print ("\nTemp: ",temp)
    
    print("checking for: ",schedule[j][0]," ",schedule[j][1],)
    
    if schedule[j][1] in temp or schedule[j][0] in temp:
        print("Overlap,",schedule[j][0]," ",schedule[j][1],"overlap in: ",temp)
        classes+=1
        
    j+=1
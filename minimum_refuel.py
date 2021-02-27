#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:30:11 2021

@author: dhruv
"""


def car_fueling(dist,miles,n,gas_stations):
    
    s = set()
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  
        # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
          
        # Find the furthest gas station we can reach
        i =0
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            i+=1
            print(i)
            curr_refill += 1
            
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank 
        curr_refill += 1
        s.add(curr_refill)
        
    return s

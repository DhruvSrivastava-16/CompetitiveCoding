# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:21:14 2021

@author: DHRUV
"""


#Dynamic Programming - Top Down Approach 
#Recursion with Memoization 


def fibo(n,dp):
    if n == 1 or n == 0:
        return n
    
    if dp[n]!=0:
        return dp[n]
    
    t = fibo(n-1,dp) + fibo(n-2,dp)
    dp[n] = t
    
    return t



#Dynamic Programming - Bottom Approach Approach 
#Recursion with Memoization 

def fibo_bu(n,dp):
    
    dp[1] = 1
    

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
        
        

n = int(input("Tell value of n: "))
dp = [0] * 100

print("ANS: ",fibo_bu(n,dp))
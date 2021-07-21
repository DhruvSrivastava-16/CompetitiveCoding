# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:26:43 2021

@author: DHRUV
"""




#Top Down Approach



def minchange(n,coins,dp):
    if n == 0:
        return 0
    
    dp[n] = min(minchange(n-i,coins,dp) for i in coins if i<=n)+1
    
    return dp[n]
    




def minchangeBU(n,coins,dp):
    for i in range(1,n+1):
        dp[i] = min(dp[i-j] for j in coins if j<=i)+1
        
    return dp[n]
    
   


n = int(input("Value: "))
coins = [1,7,10]
dp = [0]*100
print("ANS Bottom Up: ",minchangeBU(n,coins,dp))
print(dp);

dp = [0]*100
print("ANS Top Down: ",minchange(n,coins,dp))

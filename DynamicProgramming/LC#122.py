# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:04:09 2021

@author: DHRUV
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:43:39 2021

@author: DHRUV
"""


class Solution:
   def maxProfit(self, prices,n):
       if n<1:
          return 0
      
        dp[n] = max(dp[n-1],dp[n-1] + sp - bc)
        
        
        

        
prices = [7,1,5,3,6,4]
S = Solution()
S.maxProfit(prices)
dp = [0] * 30,000
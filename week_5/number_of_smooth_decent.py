"""
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
"""

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return len(prices)
        
        left = 0
        right = 1
        count = 0
        
        while right < len(prices):
            if prices[right - 1] - prices[right] == 1:
                right += 1                       
            else:
                count += (right - left) * (right - left + 1) // 2
                left = right
                right += 1            
            
            if right == len(prices):
                count += (right - left) * (right - left + 1) // 2
        return count
"""
https://leetcode.com/problems/powx-n/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float: 
        if n == 0:
            return 1
        
        if n == 1:
            return x
                        
        if n < 0:
            x = 1 / x
            n = abs(n)        
             
        if n % 2 == 0:            
            return self.myPow(x, n // 2) ** 2
        else:
            return x * (self.myPow(x, n // 2) ** 2)
            
            
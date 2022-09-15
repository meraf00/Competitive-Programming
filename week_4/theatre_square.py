"""
https://codeforces.com/problemset/problem/1/A
"""

import math

class Solution:
    def cover_theatre(self, n, m, a):                
        x = math.ceil(n / a)        
        y = math.ceil(m / a)
        
        return x * y


# take input
n, m, a = list(map(int, input().strip().split(" ")))

print(Solution().cover_theatre(n, m, a))

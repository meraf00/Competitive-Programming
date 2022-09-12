"""
https://leetcode.com/problems/h-index/
"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        max_h = 0
        
        for i, h in enumerate(citations):                 
            if i + 1 <= h:
                max_h = i + 1
                       
        return max_h
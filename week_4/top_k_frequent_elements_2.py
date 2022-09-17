"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

import heapq
from typing import List

class Compare:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq > other.freq 
    
    def __gt__(self, other):
        return self.freq < other.freq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        
        for num in nums:
            if counter.get(num):
                counter[num] += 1
            else:
                counter[num] = 1
        
        heap = []
        for key in counter.keys():
            heapq.heappush(heap, Compare(key, counter[key]))
        
        solution = []
        while k > 0:
            solution.append(heapq.heappop(heap).val)
            k -= 1
        
        return solution
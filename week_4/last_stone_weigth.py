"""
https://leetcode.com/problems/last-stone-weight/
"""


from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i, weight in enumerate(stones):
            stones[i] = -1 * weight
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            x, y = min(x, y), max(x, y)

            if x != y:
                heapq.heappush(stones, x - y)
        
        if len(stones) == 0:
            return 0
        
        return -1 * stones[0]
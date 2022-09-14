"""
https://leetcode.com/problems/top-k-frequent-words/
"""

from typing import List

class Container:
    def __init__(self, value: int):
        self.val = value
        self.freq = 1

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        
        for num in nums:
            if num_freq.get(num):
                num_freq[num].freq += 1
            else:
                num_freq[num] = Container(num)
        
        numbers = list(num_freq.values())
        numbers.sort(reverse=True, key=lambda num: num.freq)
        
        return [num.val for num in numbers[:k]]
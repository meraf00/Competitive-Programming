"""
https://leetcode.com/problems/xor-queries-of-a-subarray/description/
"""

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]
        for num in arr[1:]:
            prefix.append(prefix[-1] ^ num)
        
        output = []
        for left, right in queries: 
            if left == right:
                output.append(arr[left])
                continue

            if left == 0:
                output.append(prefix[right])
            else:
                output.append(prefix[right] ^ prefix[left - 1])
            
        return output
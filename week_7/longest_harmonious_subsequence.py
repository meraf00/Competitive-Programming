"""https://leetcode.com/problems/longest-harmonious-subsequence"""

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_length = 0
        for num in counter:
            if counter.get(num + 1):
                max_length = max(max_length, counter[num] + counter[num + 1])
        return max_length
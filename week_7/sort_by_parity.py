"""https://leetcode.com/problems/sort-array-by-parity"""

from typing import List
from functools import cmp_to_key

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def custom_compare(x, y):
            if x % 2 and y % 2:  # both odd compare reverse
                return -1 if x < y else 1
            elif x % 2 == 0 and y % 2 == 0 : # both even compare normal
                return 1 if x < y else -1
            elif x % 2: # x is odd, say odd is greater than even
                return 1
            else:
                return -1

        nums.sort(key=cmp_to_key(custom_compare))
        return nums
        
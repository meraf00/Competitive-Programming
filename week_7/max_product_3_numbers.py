"""https://leetcode.com/problems/maximum-product-of-three-numbers/"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
                  
        return max(nums[-3] * nums[-2] * nums[-1],   # all positive
            nums[-1] * nums[0] * nums[1])    # two negative one positive

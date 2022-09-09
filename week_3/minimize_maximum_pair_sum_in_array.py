from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        indexFront = 0
        indexBack = len(nums) - 1
        
        max_pair_sum = 0
        
        while indexFront < indexBack:
            max_pair_sum = max(nums[indexFront] + nums[indexBack], max_pair_sum)
            indexFront += 1
            indexBack -= 1
        return max_pair_sum
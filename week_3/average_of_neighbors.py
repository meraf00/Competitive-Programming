from typing import List


class Solution:    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()                
        new = [None] * len(nums)
        for i in range(len(nums) // 2):
            new[2*i + 1] = nums[i]
            new[2*i] = nums[i+len(nums) // 2]
        
        if new[-1] == None:
            new[-1] = nums[-1]
        return new
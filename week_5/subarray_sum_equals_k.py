"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""

from typing import List

class Solution:  
    # not my idea, it's fast!!  
    def subarraySum(self, nums: List[int], k: int) -> int:        
        prefix_sum = [nums[0]] * len(nums)
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        counter = {}
        total = 0
        for i in range(len(nums)):
            if prefix_sum[i] == k:
                total += 1
            
            if counter.get(prefix_sum[i] - k):
                total += counter[prefix_sum[i] - k]
            
            if counter.get(prefix_sum[i]):
                counter[prefix_sum[i]] += 1
            else:
                counter[prefix_sum[i]] = 1
        return total
    
    
    # TLE
    def _subarraySum(self, nums: List[int], k: int) -> int:
        cummulative = 0
        for i in range(len(nums)):
            nums[i] += cummulative
            cummulative = nums[i]        
        
        total = 0
                        
        for right in range(len(nums)):                                      
            for left in range(right):
                if nums[right] - nums[left] == k:
                    total += 1         
            if nums[right] == k:
                total += 1                     
        
        return total
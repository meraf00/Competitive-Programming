"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""


from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = right = 0
        
        sum_ = 0
        max_freq = 0
        while right < len(nums):
            sum_ += nums[right]
            
            if nums[right] * (right - left + 1) - sum_ > k:
                sum_ -= nums[left]
                left += 1                            
            
            max_freq = max(max_freq, right - left + 1)
            
            right += 1
        
        return max_freq

    # trial 1 - TLE
    def _maxFrequency(self, nums: List[int], k: int) -> int:
        counter = {}
        
        for num in nums:
            if counter.get(num):
                counter[num] += 1
                continue
                
            counter[num] = 1
        
        max_freq = 0
        for num in sorted(counter.keys()):
            available = k        
            n = num - 1
            deficit = num - n
            freq = counter[num]
            while n > 0 and deficit <= available:                
                if not counter.get(n):
                    n -= 1
                    deficit = num - n
                    continue
                    
                if available >= deficit * counter[n]:
                    available -= deficit * counter[n]
                    freq += counter[n]
                    n -= 1
                    deficit = num - n                    
                    
                else:
                    freq += available // deficit
                    break
            max_freq = max(max_freq, freq)    
                    
        return max_freq
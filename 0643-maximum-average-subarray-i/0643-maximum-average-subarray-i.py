class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        
        max_sum = float("-inf")        
        current_sum = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            if right - left + 1 == k:                
                max_sum = max(max_sum, current_sum)
                current_sum -= nums[left]
                left += 1
        
        return max_sum / k
        
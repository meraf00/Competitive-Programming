class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_element = float('inf')
        
        max_difference = 0
        
        for num in nums:
            min_element = min(min_element, num)
            
            max_difference = max(num - min_element, max_difference)
        
        if max_difference <= 0:
            return -1
        
        return max_difference
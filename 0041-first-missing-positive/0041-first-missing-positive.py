class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        
        while i < n:
            correct_pos = nums[i] - 1
            
            if 0 <= correct_pos < n and nums[correct_pos] != nums[i] and correct_pos != i:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            
            else:
                i += 1
        
        for i, num in enumerate(nums):
            if nums[i] - 1 != i:
                return i + 1
        
        return n + 1
        
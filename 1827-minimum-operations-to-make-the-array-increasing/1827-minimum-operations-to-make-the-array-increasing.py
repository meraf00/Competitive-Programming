class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:                
                new_val = nums[i - 1] + 1
                operations += new_val - nums[i]
                nums[i] = new_val 
        
        return operations
                
                
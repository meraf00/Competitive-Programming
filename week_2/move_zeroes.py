class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeroIndex = 0        
        i = 0
        while i < len(nums):
            if nums[i] != 0:                                
                nums[nonzeroIndex] = nums[i]
                nonzeroIndex += 1
                
            i += 1
                
        while nonzeroIndex < len(nums):
            nums[nonzeroIndex] = 0
            nonzeroIndex += 1
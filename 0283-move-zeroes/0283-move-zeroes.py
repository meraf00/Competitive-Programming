class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        for holder, num in enumerate(nums):
            if num == 0:
                break
        
        seeker = holder + 1
        
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            
            seeker += 1
        
        
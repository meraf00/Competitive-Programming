class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        copy = [0] * len(nums)
        
        for index, num in enumerate(nums):
            copy[(index + k) % len(nums)] = num
        
        for i in range(len(nums)):
            nums[i] = copy[i]
            
        
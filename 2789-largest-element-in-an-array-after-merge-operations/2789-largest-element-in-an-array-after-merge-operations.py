class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:  
        length = len(nums)
        
        max_merged = nums[-1]
        
        for i in range(length - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nums[i] += nums[i + 1]
            
            max_merged = max(nums[i], max_merged)
            
        
        return max_merged

"""
[5,3,3]
[1,2,3,4,5,6,7]
[7,6,5,4,3,2,1]
[1,2,3,6,3,5,7]
[34,95,50,12,25,100,21,3,25,16,76,73,93,46,18]
[40,15,35,98,77,79,24,62,53,84,97,16,30,22,49]
"""
            
            
            
            
            
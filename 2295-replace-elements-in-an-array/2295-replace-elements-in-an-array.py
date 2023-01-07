class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        nums_as_dict = {}
        
        # store the index of each number in nums_as_dict
        for index, num in enumerate(nums):
            nums_as_dict[num] = index
        
         
        for original, replacer in operations:            
            index = nums_as_dict[original]
            del nums_as_dict[original]
            nums_as_dict[replacer] = index
            nums[index] = replacer
            
        return nums
        
        
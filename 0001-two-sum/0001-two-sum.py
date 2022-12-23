class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        
        for index, num in enumerate(nums):
            if num in nums_d and 2 * num ==  target:
                return [index, nums_d[num]]
                                
            nums_d[num] = index
            
            num_2 = target - num
            if num_2 != num and num_2 in nums_d:
                index_2 = nums_d[num_2]
                
                return [index, index_2]
            
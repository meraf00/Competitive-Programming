class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        length = len(nums)
        
        if length <= 2:
            return True
        
        for i in range(1, length):
            if nums[i - 1] + nums[i] >= m:
                return True
        
        return False
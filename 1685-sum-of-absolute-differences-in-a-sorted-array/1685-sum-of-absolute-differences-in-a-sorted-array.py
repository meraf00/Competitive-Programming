class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
                
        result = [0] * n
        
        for i in range(1, n):
            gap = nums[i] - nums[i - 1]
            result[i] = gap * i + result[i - 1]
        
        prev = 0
        for i in range(n - 2, -1, -1):
            gap = nums[i + 1] - nums[i]            
            prev = gap * (n - i - 1) + prev
            result[i] += prev
        
        return result
            
        
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n_nums = len(nums)
        
        nums.sort()
        
        count = 0
        
        for i in range(n_nums):
            for j in range(i + 1, n_nums):
                idx = bisect_left(nums, nums[i] + nums[j])
                
                if idx > j:                
                    count += idx - j - 1
                
        
        return count
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        largest_num = max(nums)
        
        nums.sort()
        
        subtracted = 0
        
        op_count = 0
        
        for num in nums:                        
            num = max(0, num - subtracted)
            
            if num == 0:
                continue
            
            subtracted += num
            op_count += 1
            
        
        return op_count
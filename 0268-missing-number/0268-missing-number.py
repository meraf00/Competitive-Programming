class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        max_ = float('-inf')
        
        actual_sum = 0
        zero_exists = False
        
        for n in nums:
            if max_ < n:
                max_ = n
            if n == 0:
                zero_exists = True
                
            actual_sum += n
                
        expected_sum = max_ * (max_ + 1) // 2        
        
        missing = expected_sum - actual_sum
        
        if missing == 0 and zero_exists:
            return max_ + 1
        
        return missing
        
        
        
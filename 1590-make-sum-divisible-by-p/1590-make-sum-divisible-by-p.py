class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)   
        
        r = sum(nums) % p
                        
        seen = {0: -1}        
        
        running_sum = 0                
        min_subarray = float('inf')              
        
        for right in range(n):
            running_sum += nums[right]
            
            curr = running_sum % p
            
            seen[curr] = right
            
            if (curr - r) % p in seen: 
                size = right - seen[(curr - r) % p]
                min_subarray = min(size, min_subarray)                        
            
            
        
        if min_subarray < n:
            return min_subarray
        
        return -1
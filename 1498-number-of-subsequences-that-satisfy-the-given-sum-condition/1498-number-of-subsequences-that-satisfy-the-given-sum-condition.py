class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7        
        n = len(nums)
        
        nums.sort()                       
                
        count = 0
        
        for left, num in enumerate(nums):
            right = bisect_right(nums, target - num)
                        
            if right <= left:
                break
            
            count += pow(2, right - left - 1, mod) 
            count %= mod
            
        return count
            
        
                
                
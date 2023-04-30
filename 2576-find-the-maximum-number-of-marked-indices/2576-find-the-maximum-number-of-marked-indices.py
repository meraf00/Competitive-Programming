class Solution:    
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        
        length = len(nums)
        
        
        def check(k):            
            for i in range(k):                
                if nums[i] * 2 > nums[length - (k - i)]:                    
                    return False
            
            return True
                    
        
        low = 0
        high = len(nums) // 2
        marked = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                marked = max(mid * 2, marked)
                low = mid + 1
            
            else:
                high = mid - 1
        
        return marked
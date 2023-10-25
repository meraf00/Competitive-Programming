class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        
        
        while low <= high:
            mid = (low + high) // 2
            
            current = sum(map(lambda x: ceil(x / mid), nums))
                        
            if current > threshold:
                low = mid + 1
            
            else:
                high = mid - 1
        
        
        return low
                
        
        
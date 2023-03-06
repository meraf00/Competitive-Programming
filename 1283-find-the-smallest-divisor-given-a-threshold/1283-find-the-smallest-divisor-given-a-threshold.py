class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
                
        
        while low <= high:
            mid = low + (high - low) // 2
            
            current = sum(map(lambda x: ceil(x/mid), nums))
            
            if current > threshold:
                low = mid + 1
            
            else:
                high = mid - 1
        
        current = sum(map(lambda x: ceil(x / low), nums))
        
        if current <= threshold:
            return low
        
        return high
        
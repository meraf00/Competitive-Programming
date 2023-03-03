class Solution:
    def mySqrt(self, x: int) -> int:        
        low = 0
        high = x
        
        while low <= high:            
            mid = (low + high) // 2
            
            result = mid * mid
            
            if result < x:
                low = mid + 1
            
            elif result > x:
                high = mid - 1
            
            else:
                return mid
        
        if result > x:
            return mid - 1
        
        return mid
            
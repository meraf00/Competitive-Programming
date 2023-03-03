class Solution:
    def mySqrt(self, x: int) -> int:        
        low = 0
        high = x
        
        def binarySearch(low, high):
            if low >= high:
                return high
            
            mid = low + (high - low) // 2
            
            result = mid * mid

            if result > x:
                return binarySearch(low, mid - 1)
            
            elif result < x:
                return binarySearch(mid + 1, high)
            
            else:
                return mid
        
        sqrt = binarySearch(low, high)
        
        if sqrt * sqrt > x:
            return sqrt - 1
        
        return sqrt
        
            
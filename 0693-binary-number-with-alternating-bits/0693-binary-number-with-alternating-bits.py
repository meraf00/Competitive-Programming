class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        last_seen = n & 1
        n >>= 1
        
        while n:
            if n & 1 == last_seen:
                return False
            
            last_seen = n & 1
            n >>= 1 
            
            
        return True
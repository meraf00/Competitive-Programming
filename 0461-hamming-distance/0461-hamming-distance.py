class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        
        count = 0
        
        while xor:
            if xor & 1:
                count += 1
            xor >>= 1
        
        return count
        
        
        
        
        
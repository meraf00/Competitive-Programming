class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0        
        
        for i in range(32):
            if n & 1:
                reversed_bits = reversed_bits | (1 << (31 - i))
            
            n >>= 1
            
        
        return reversed_bits
            
        
        
class Solution:
    def findComplement(self, num: int) -> int:
        n = 1
        
        for i in range(num.bit_length()):
            num ^= n
            n <<= 1                    
            
        
        return num
        
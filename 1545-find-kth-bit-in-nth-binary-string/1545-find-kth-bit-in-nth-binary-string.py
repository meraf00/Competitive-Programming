class Solution:
    evaluated = {0: "0", 1:"1", 2:"1"}
    
    def isPowerOf2(self, k):
        return (k & (k - 1)) == 0
    
    def find(self, n, k):
        
        if k in self.evaluated:
            return self.evaluated[k]
        
        # if 2**n - 1 - k in self.evaluated:
        #     self.evaluated[k] = "0" if self.evaluated[2**n - 1 - k] == "1" else "1"
        #     return self.evaluated[k]
        
        if self.isPowerOf2(k + 1):            
            self.evaluated[k] = "1"
            return self.evaluated[k]
                
        
        first_set_bit = k.bit_length() - 1        
        
        mirror = 2 ** first_set_bit - 1                
        
        result = self.find(n, 2 * mirror - k)
        
        self.evaluated[2 * mirror - k] = result
        
        self.evaluated[k] = "0" if result == "1" else "1"                
        
        return self.evaluated[k]
            
    def findKthBit(self, n: int, k: int) -> str:
        
        return self.find(n, k - 1)
        
        
        
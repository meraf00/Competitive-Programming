class Solution:   
    evaluated = {0: False, 1: True}
    
    def isPowerOf2(self, n):
        return (n & (n - 1)) == 2
    
    def getKth(self, index):
        if index in self.evaluated:
            return self.evaluated[index]
        
        if self.isPowerOf2(index + 1):
            if (index + 1) % 4 == 0:
                self.evaluated[index] = 0
            else:
                self.evaluated[index] = 1
            return self.evaluated[index]
        
        nearest_power_of_2 = 2 ** (index.bit_length() - 1)
        
        mirror_index = index - nearest_power_of_2
                
        self.evaluated[index] = not self.getKth(mirror_index)
        
        return self.evaluated[index]
        
        
    def kthGrammar(self, n: int, k: int) -> int:
        
        return int(self.getKth(k - 1))
        
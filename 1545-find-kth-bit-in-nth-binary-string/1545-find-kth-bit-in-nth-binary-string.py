class Solution:
    evaluated = {1: ["0"]}            
        
    def buildString(self, n):
        if n in self.evaluated:
            return self.evaluated[n]                
        
        string = list(self.buildString(n - 1))
        
        second_part = reversed(["1" if char == "0" else "0" for char in string ])
        
        string.append("1")
        
        string.extend(second_part)                
        
        self.evaluated[n] = string
        
        return string
        
        
    def findKthBit(self, n: int, k: int) -> str:
        
        return self.buildString(n)[k - 1]
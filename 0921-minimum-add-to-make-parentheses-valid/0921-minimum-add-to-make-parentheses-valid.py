class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        
        addition_count = 0
        
        for char in s:
            if char == "(":
                open_count += 1
            
            elif open_count > 0:
                open_count -= 1
            
            else:
                addition_count += 1
        
        addition_count += open_count
        
        return addition_count
            
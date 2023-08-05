class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        counter = 0
        
        for char in s:
            if char == "(":
                stack.append(0)
            
            elif stack:
                stack.pop()
            
            else:
                counter += 1
        
        counter += len(stack)
        
        return counter
            
class Solution:
    def removeStars(self, s: str) -> str:
        string = []
        
        for char in s:
            if char == "*":
                string.pop()
            
            else:
                string.append(char)
        
        return ''.join(string)
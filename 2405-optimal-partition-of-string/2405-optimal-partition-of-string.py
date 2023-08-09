class Solution:
    def partitionString(self, s: str) -> int:
        length = len(s) - 1
        
        current = set()
        
        count = 0
        
        for idx, char in enumerate(s):                        
            if char not in current:
                current.add(char)                                
            
            else:
                current.clear()
                current.add(char)
                count += 1                                
        
        return count + 1
                        
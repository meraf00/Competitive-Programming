class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        length = len(s)
        
        max_count = 1
        
        unique_substrings = set()        
        
        def backtrack(char_idx):
            nonlocal max_count
            
            if char_idx >= length: 
                max_count = max(len(unique_substrings), max_count)                
                return                        
            
            for i in range(char_idx + 1, length + 1):
                substring = s[char_idx: i]
                
                if substring not in unique_substrings:
                    unique_substrings.add(substring)                    
                    backtrack(i)                    
                    unique_substrings.remove(substring)                                
        
        backtrack(0)
        
        return max_count
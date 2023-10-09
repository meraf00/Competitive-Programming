class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
                
        for i in range(len(haystack) - len(needle) + 1):
            k = i
            
            for j in range(len(needle)):                
                if haystack[k] != needle[j]:
                    break
                    
                k += 1
                
            else:
                return i
        
        return -1 
        
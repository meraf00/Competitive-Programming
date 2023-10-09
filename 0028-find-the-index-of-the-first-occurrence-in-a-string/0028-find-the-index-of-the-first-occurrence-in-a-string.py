class Solution:    
    def strStr(self, haystack: str, needle: str) -> int:        
        len_n = len(needle)
        
        lps = [0] * len_n
                
        i, j = 0, 1
        
        while j < len_n and i < len_n:
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            
            else:
                if i == 0:
                    j += 1
                
                else:
                    i = lps[i - 1]
        
        i = 0
        j = 0
        
        len_h = len(haystack)
        
        while j < len_h and i < len_n:
            if needle[i] == haystack[j]:
                i += 1
                j += 1
                
                if i >= len_n:
                    return j - i
            
            else:
                if i == 0:
                    j += 1
                
                else:
                    i = lps[i - 1]
        
        return -1
                    
            
            
        
        
        
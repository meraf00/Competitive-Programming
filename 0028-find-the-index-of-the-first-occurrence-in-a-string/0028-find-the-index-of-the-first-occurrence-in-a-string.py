class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        left = 0
        
        for right in range(haystack_length):           
            if right - left + 1 == needle_length:                
                if haystack[left : right + 1] == needle:
                    return left
                
                left += 1
        
        return -1
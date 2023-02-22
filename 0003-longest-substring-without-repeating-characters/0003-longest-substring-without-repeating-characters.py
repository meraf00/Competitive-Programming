class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        
        unique_chars = set()
        max_size = 0
        
        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            
            unique_chars.add(s[right])
            
            max_size = max(len(unique_chars), max_size)
        
        return max_size
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import List


class Solution:
    def isUnique(self, s: str) -> bool:
        charList = list(s)
        charList.sort()
        
        for i in range(len(charList) - 1):
            if charList[i + 1] == charList[i]:
                return False
        return True
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        
        max_length = 0
        while right < len(s):                                     
            if self.isUnique(s[left:right+1]):                   
                max_length = max(max_length, len(s[left:right+1]))
                right += 1                
            else:       
                left += 1
                while not self.isUnique(s[left:right+1]):
                    left += 1
                        
        return max_length
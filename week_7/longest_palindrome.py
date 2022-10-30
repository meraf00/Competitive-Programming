"""https://leetcode.com/problems/longest-palindrome"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        
        length = 0
        max_non_even = None
        for letter, count in counter.items():
            if count % 2 == 0:
                length += count
            elif max_non_even == None:
                max_non_even = letter
            elif count >= counter[max_non_even]:
                length += counter[max_non_even] - 1
                max_non_even = letter
            else:
                length += count - 1
                
        return length + counter[max_non_even]
"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        left = right = 0
        current = 0
        while right < k:
            if s[right] in vowels:
                current += 1
            right += 1

        max_ = current
        while right < len(s):
            if s[right] in vowels:
                current += 1
            if s[left] in vowels:
                current -= 1
            right += 1
            left += 1
            max_ = max(max_, current)
        return max_

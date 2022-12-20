"""https://leetcode.com/problems/find-the-difference"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for c in letters:
            if s.count(c) != t.count(c):
                return c
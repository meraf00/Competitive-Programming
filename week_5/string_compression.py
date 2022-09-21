"""
https://leetcode.com/problems/string-compression/submissions/
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0

        while right < len(chars):
            if left < right and chars[left] != chars[right]:
                if right - left > 1:
                    del chars[left + 1: right]
                    count = right - left
                    right = left + 1
                    for digit in reversed(str(count)):
                        chars.insert(left + 1, digit)
                        right += 1
                left = right


            if chars[left] == chars[right]:
                right += 1

        if right > left + 1:
            del chars[left + 1: right]
            for digit in reversed(str(right - left)):
                chars.insert(left + 1, digit)
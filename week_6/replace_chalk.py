"""
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [chalk[0]]

        for c in chalk[1:]:
            prefix.append(prefix[-1] + c)

        k = k % prefix[-1]

        for i in range(len(prefix)):
            if prefix[i] > k:
                return i

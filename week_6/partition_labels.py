"""
https://leetcode.com/problems/partition-labels/
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farthest_encounter = {}

        for i in range(len(s) - 1, -1, -1):
            if farthest_encounter.get(s[i]):
                continue
            farthest_encounter[s[i]] = i

        output = []
        left = right = 0
        bound = farthest_encounter[s[right]]
        while right < len(s):
            if right < bound:
                bound = max(farthest_encounter[s[right]], bound)
            else:
                output.append(right - left + 1)
                left = right + 1
                if left < len(s):
                    bound = farthest_encounter[s[left]]
            right += 1
        return output

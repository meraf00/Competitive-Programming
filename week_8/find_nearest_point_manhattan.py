"""https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/submissions/862923272/"""

from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1
        for i, point in enumerate(points):            
            x2, y2 = point
            if x == x2 or y == y2:
                distance = abs(x - x2) + abs(y - y2)
                if distance < min_distance:
                    min_index = i
                    min_distance = distance
        return min_index
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        max_gap = 0
        
        for i in range(1, len(points)):
            gap = points[i][0] - points[i - 1][0]
            max_gap = max(gap, max_gap)
        
        return max_gap
            
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_pts = sorted(map(lambda pt: pt[0], points))
        
        max_gap = 0
        
        for i in range(1, len(sorted_pts)):
            gap = sorted_pts[i] - sorted_pts[i - 1]
            max_gap = max(gap, max_gap)
        
        return max_gap
            
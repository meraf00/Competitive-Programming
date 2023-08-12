class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end point        
        points.sort(key = lambda x:x[1])
        
        arrow_count = 1
        
        last_interval_end = points[0][1]
        
        for start, end in points:
            if start <= last_interval_end:
                continue
            
            last_interval_end = end
            
            arrow_count += 1
        
        return arrow_count
            
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        rows = len(wall)
        cols = len(wall[0])
        
        
        wall_width = sum(wall[0])        
        brick_ends = defaultdict(int)

        
        for row in wall:
            prev_end = 0
            for width in row:
                end = prev_end + width - 1                
                
                if end == wall_width - 1:
                    break
                    
                brick_ends[end] += 1                
                prev_end += width
        
        
        if not brick_ends:
            return rows        
        
        return rows - max(brick_ends.values())
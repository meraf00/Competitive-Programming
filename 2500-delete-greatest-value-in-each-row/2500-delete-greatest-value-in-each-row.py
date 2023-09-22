class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        for row in grid:
            for i in range(cols):
                row[i] *= -1
            
            heapify(row)
                                
        ans = 0
        for _ in range(cols):
            current_max = float('-inf')
            for row in grid:
                current_max = max(-heappop(row), current_max)
            ans += current_max
        
        return ans
            
            
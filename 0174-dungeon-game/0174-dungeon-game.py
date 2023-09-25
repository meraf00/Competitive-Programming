class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        
        dp = [[0] * cols for _ in range(rows)]
        
        dp[-1][-1] = dungeon[-1][-1]
        
        for col in range(cols - 2, -1, -1):
            dp[-1][col] += min(dp[-1][col + 1], 0) + dungeon[-1][col]
        
        for row in range(rows - 2, -1, -1):
            dp[row][-1] += min(dp[row + 1][-1], 0) + dungeon[row][-1]       

        
        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                health = dungeon[row][col]
                
                min_health_required = max(
                    min(dp[row + 1][col], 0) + health, 
                    min(dp[row][col + 1], 0) + health
                    )
                
                dp[row][col] = min_health_required
        
        
            
        if dp[0][0] >= 0:
            return 1
        
        return 1 - dp[0][0]

    
"""
[[1,-2,3],[2,-2,-2]]
[[1,-3,3],[0,-2,0],[-3,-3,-3]]
[[0,0,0],[1,1,-1]]
[[0,1,0],[1,1,-1]]
[[0,0,1],[1,1,-1]]
[[0,1,1],[1,1,-1]]
[[0,0,1],[0,1,-1]]
[[0,0,1],[-1,1,-1]]
[[-2,-3,3],[-5,-10,1],[10,30,-5]]
[[0]]
[[-2,-3,-30],[-5,-10,1],[10,30,-5]]
[[-2,-3,-30],[-5,-10,1],[10,30,-5],[1,2,3]]
[[-200]]
[[1,-2,3],[2,-2,-2]]
"""
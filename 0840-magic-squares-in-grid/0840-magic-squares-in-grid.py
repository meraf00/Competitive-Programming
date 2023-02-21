class Solution:
    def isValid(self, grid, top, left):
        nums = set()
        nums.add(grid[top][left])
        nums.add(grid[top][left+1])
        nums.add(grid[top][left+2])
        nums.add(grid[top+1][left])
        nums.add(grid[top+1][left+1])
        nums.add(grid[top+1][left+2])
        nums.add(grid[top+2][left])
        nums.add(grid[top+2][left+1])
        nums.add(grid[top+2][left+2])        
        return len(nums) == 9 and min(nums) == 1 and max(nums) == 9
    def isMajic(self, grid, top, left):
        if not self.isValid(grid, top, left):
            return False
        
        target = grid[top][left] + grid[top][left+1] + grid[top][left+2]
        
        for row in range(3):
            if grid[top + row][left] + grid[top + row][left + 1] + grid[top + row][left+2] != target: return False
        
        for col in range(3):
            if grid[top][left + col] + grid[top + 1][left + col] + grid[top + 2][left+col] != target: return False
        
        
        if grid[top][left] + grid[top + 1][left + 1] + grid[top + 2][left+2] != target: return False
        if grid[top+2][left] + grid[top + 1][left + 1] + grid[top][left+2] != target: return False
        return True
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        counter = 0
        for row in range(rows-2):
            for col in range(cols-2):
                if self.isMajic(grid, row, col):
                    counter += 1
        return counter
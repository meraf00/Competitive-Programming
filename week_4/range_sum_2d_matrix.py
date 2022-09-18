"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        self.cummulative_sum()
    
    def cummulative_sum(self): 
        """row cummulative"""
                
        for r in range(len(self.matrix)):
            cummulative = 0
            for c in range(len(self.matrix[0])):
                self.matrix[r][c] += cummulative
                cummulative = self.matrix[r][c]        
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0        
        for r in range(row1, row2 + 1):
            if col1 != 0:
                total += self.matrix[r][col2] - self.matrix[r][col1 - 1]
            else:
                total += self.matrix[r][col2]
                
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
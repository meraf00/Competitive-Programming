class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        sum = 0
        
        for r in range(rows):
            for c in range(cols):
                if r == c:
                    sum += mat[r][c]
                
                elif r + c == rows - 1:
                    sum += mat[r][c]
        
        return sum
                    
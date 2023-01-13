class Solution:    
    def findDuplicateIn3x3(self, board, row_begin, col_begin):
        nums = set()
        for row_idx in range(row_begin, row_begin + 3):
            for col_idx in range(col_begin, col_begin + 3):
                num = board[row_idx][col_idx]
                
                if num == ".":
                    continue
                    
                if num in nums: 
                    return True                
                nums.add(num)
        
        return False        
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        # check 1st and 2nd rule
        rows_ = defaultdict(set)
        cols_ = defaultdict(set)
        
        for row_idx in range(rows):
            for col_idx in range(cols):
                num = board[row_idx][col_idx]
                if num == ".":
                    continue
                    
                if num in rows_[row_idx]:                    
                    return False
                
                if num in cols_[col_idx]:
                    return False
                
                rows_[row_idx].add(num)
                cols_[col_idx].add(num)
                    
        # check 3rd rule
        for row_idx in range(0, 9, 3):
            for col_idx in range(0, 9, 3):
                if self.findDuplicateIn3x3(board, row_idx, col_idx):
                    return False
        
        return True
        
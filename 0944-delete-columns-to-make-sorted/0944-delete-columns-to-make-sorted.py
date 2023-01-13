class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        
        num_of_columns_to_delete = 0
        
        for col_idx in range(cols):
            for row_idx in range(rows - 1):
                if strs[row_idx][col_idx] > strs[row_idx + 1][col_idx]:
                    num_of_columns_to_delete += 1
                    break
        
        
        return num_of_columns_to_delete
            
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)            
        
        for row_idx, row in enumerate(triangle):
            if row_idx == 0:
                continue  
            
            prev_row = triangle[row_idx - 1]
            
            prev_row.append(float('inf'))
                                    
            for idx, val in enumerate(row):                                                          
                row[idx] += min(prev_row[idx - 1], prev_row[idx])                                                
        
        return min(triangle[-1])
        
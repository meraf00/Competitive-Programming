class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        grid = [[] for _ in range(numRows)]
        
        n_chars = len(s)
        
        idx = 0                
        col = 0
        while idx < n_chars:
            
            if col % (numRows - 1) == 0:
                for row in range(numRows):
                    if idx >= n_chars:
                        break
                    grid[row].append(s[idx])
                    idx += 1            

            else:
                for row in range(numRows):
                    if idx >= n_chars:
                        break
                        
                    if numRows - col - 1 == row:                        
                        grid[row].append(s[idx])
                        idx += 1  
                    
                    else:
                        grid[row].append("")
                        
            
            col = (col + 1) % (numRows - 1)

        output = []
        for row in grid:
            output.append("".join(row))
        return "".join(output)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:        
        prev = [1] * (rowIndex + 1)
        curr = [1] * (rowIndex + 1)
        
        for i in range(rowIndex + 1):
            for j in range(1, i):
                curr[j] = prev[j - 1] + prev[j]
            
            prev, curr = curr, prev
                    
        return prev
                
        
        
        
        
        
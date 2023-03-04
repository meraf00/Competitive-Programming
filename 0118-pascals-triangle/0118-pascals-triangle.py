class Solution:  
    evaluated = {0: [1]}
    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in self.evaluated:
            return self.evaluated[rowIndex]
        
        row = [1]
        
        prev = self.getRow(rowIndex - 1)
        
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i+1])
        
        row.append(1)
        
        self.evaluated[rowIndex] = row
        
        return row
            
            
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            rows.append(self.getRow(i))
            
        return rows
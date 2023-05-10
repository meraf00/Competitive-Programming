class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        k -= 1
        
        for row in matrix:
            heapify(row)
        
        heapify(matrix)
        
        while k:                         
            row = heappop(matrix)            
            heappop(row)
            if row:
                heappush(matrix, row)                        
            k -= 1
        
        return matrix[0][0]
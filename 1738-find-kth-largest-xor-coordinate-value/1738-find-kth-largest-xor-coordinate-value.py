class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        kth_largest = [matrix[0][0]]
        
        
        for col in range(1, cols):
            matrix[0][col] ^= matrix[0][col - 1] 
            
            heappush(kth_largest, matrix[0][col])
            
            while len(kth_largest) > k:
                heappop(kth_largest)
        
        for row in range(1, rows):
            matrix[row][0] ^= matrix[row - 1][0]  
            
            heappush(kth_largest, matrix[row][0])
            
            while len(kth_largest) > k:
                heappop(kth_largest)
        
        
        for row in range(1, rows):
            for col in range(1, cols):
                matrix[row][col] ^= matrix[row - 1][col] ^ matrix[row - 1][col - 1] ^ matrix[row][col - 1]
                heappush(kth_largest, matrix[row][col])
            
                while len(kth_largest) > k:
                    heappop(kth_largest)
        
        
        return kth_largest[0]
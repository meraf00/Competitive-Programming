class Solution:
    def minOperations(self, n: int) -> int:                
        ops = 0
        
        for i in range(1, n, 2):
            ops += n - i
        
        return ops
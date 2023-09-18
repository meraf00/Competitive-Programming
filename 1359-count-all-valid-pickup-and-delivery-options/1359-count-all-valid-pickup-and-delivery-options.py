class Solution:
    def countOrders(self, n: int) -> int:
        MODULO = 10 ** 9 + 7
        
        if n == 1:            
            return 1
    
        pairs = n * 2
        
        arrangements = pairs - 1
        
        count = self.countOrders(n - 1)
        
        count = (count * pairs * arrangements) // 2        
        
        return count % MODULO
        
        
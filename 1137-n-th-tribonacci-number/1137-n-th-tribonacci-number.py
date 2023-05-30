class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        
        t_0 = 0
        t_1 = 1
        t_2 = 1
        
        for _ in range(n - 2):
            result = t_0 + t_1 + t_2
            
            t_0 = t_1
            t_1 = t_2
            t_2 = result                        
        
        
        return t_2
            
        
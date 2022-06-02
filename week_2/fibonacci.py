class Solution:
    def fib(self, n: int) -> int:                
        n_2, n_1 = 0, 1
        i = 0
        while i < n:            
            n_2, n_1 = n_1, n_2 + n_1             
            i += 1
        
        return n_2
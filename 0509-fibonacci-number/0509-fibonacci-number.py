class Solution:        
    computed = {0:0, 1:1}
    
    def fib(self, n: int) -> int:            
        if n in self.computed:
            return self.computed[n]
        
        num_1 = self.fib(n - 1)
        # self.computed[n - 1] = num_1
        
        num_2 = self.fib(n - 2)
        # self.computed[n - 2] = num_2
        
        self.computed[n] = num_1 + num_2
        
        return self.computed[n]
        
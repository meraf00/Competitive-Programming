class Solution:
    computed = {0:0, 1:1}
    
    def fib(self, n: int) -> int:
        computed = self.computed
        
        if n in computed:
            return computed[n]
        
        num_1 = self.fib(n - 1)
        computed[n - 1] = num_1
        
        num_2 = self.fib(n - 2)
        computed[n - 2] = num_2
        
        computed[n] = num_1 + num_2
        
        return computed[n]
        
class Solution:
    computed = {1:1, 2:2}
    
    def climbStairs(self, n: int) -> int:
        if n in self.computed:
            return self.computed[n]
        
        num_1 = self.climbStairs(n - 1)
        
        num_2 = self.climbStairs(n - 2)
        
        self.computed[n] = num_1 + num_2
        
        return self.computed[n]
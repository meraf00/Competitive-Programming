class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        
        memo = {
            0: 0,
            1: 1
        }
        
        max_value = float('-inf')
        
        def generate(n):
            nonlocal max_value
            if n in memo:    
                max_value = max(memo[n], max_value)
                return memo[n]
                                
            i = n // 2
            
            # odd
            if n & 1:                
                memo[n] = generate(i) + generate(i + 1)
            
            # even
            else:                      
                memo[n] = generate(i)                                        
            
            max_value = max(memo[n], max_value)
            
            return memo[n] 
        
        
        
        for i in range(n + 1):        
            generate(i)
               
            
        
        return max_value
            
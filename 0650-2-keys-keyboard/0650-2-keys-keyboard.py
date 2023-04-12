class Solution:                    
    def minSteps(self, n: int) -> int:
        prime_factors = []
        
        i = 2
        while n > 1:
            while n % i == 0:
                n //= i
                prime_factors.append(i)
            
            i += 1
        
                        
        return sum(prime_factors)
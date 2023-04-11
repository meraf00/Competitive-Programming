class Solution:          
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        
        for n in nums:
            current_factors = set()
            
            i = 2
            while i <= n:
                while n % i == 0:
                    n //= i
                    factors.add(i)

                i += 1
            
            factors = factors.union(current_factors)
        
        return len(factors)
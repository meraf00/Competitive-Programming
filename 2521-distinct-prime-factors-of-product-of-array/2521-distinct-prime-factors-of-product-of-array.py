class Solution:
    def seive(self, n):        
        primes = [1] * n
        primes[0] = primes[1] = 0
        
        for i in range(int(sqrt(n)) + 1):
            if not primes[i]:
                continue
            
            j = i
            while j <= n:
                primes[j] = 0
                j += i            
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        
        for n in nums:                        
            i = 2
            while i <= n:
                while n % i == 0:
                    n //= i
                    factors.add(i)

                i += 1                        
        
        return len(factors)
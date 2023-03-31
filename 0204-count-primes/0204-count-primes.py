class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        primes = [True] * n 
        primes[0] = primes[1] = False
        
        
        j = 4
        while j < n:
            primes[j] = False
            j += 2
        
        
        for i in range(3, int(sqrt(n)) + 1, 2):            
            if primes[i]:                
                j = i * i
                while j < n:
                    primes[j] = False
                    j += i
                    
        return sum(primes)
                
            
class DSU:
    def __init__(self, size):
        self.reps = {i: i for i in range(size)}
        self.rank = {i: 1 for i in range(size)}
        
        
    def find(self, member):
        root = member
        while root != self.reps[root]:
            root = self.reps[root]


        while member != root:
            parent = self.reps[member]
            self.reps[member] = root
            member = parent

        return root


    def union(self, x, y):
        xRep = self.find(x)
        yRep = self.find(y)


        if xRep == yRep:
            return

        if self.rank[xRep] >= self.rank[yRep]:
            self.reps[yRep] = xRep
            self.rank[xRep] += self.rank[yRep]

        else:
            self.reps[xRep] = yRep
            self.rank[yRep] += self.rank[xRep]
                                                    

class Solution:
    def primeFactors(self, n):
        factors = set()
        
        i = 2        
        while i * i <= n:
            if n % i == 0:
                n //= i
                factors.add(i)
            
            else:
                i += 1
                
        if n > 1:
            factors.add(n)
               
        return factors
            
    
    def largestComponentSize(self, nums: List[int]) -> int:
        n_nums = len(nums)
        
        dsu = DSU(n_nums)
        
        primes = defaultdict(list)
        
        for idx, num in enumerate(nums):
            factors = self.primeFactors(num)

            for prime in factors:
                primes[prime].append(idx)
                
        
        for indexes in primes.values():            
            for i in range(1, len(indexes)):
                dsu.union(indexes[i - 1], indexes[i])                
            
        
        largest_group = 0
        
        for i in range(n_nums):
            rep = dsu.find(i)
            largest_group = max(largest_group, dsu.rank[rep])
            
            
        return largest_group
        
        
        
        
        
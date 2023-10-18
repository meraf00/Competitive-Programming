class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool: 
        if len(nums) == 1:
            return True
        
        @cache
        def prime_factor(num):
            if num <= 1:
                return []
            
            i = 2
            
            factors = []
            while i * i <= num:
                if num % i == 0:  
                    factors.append(i)
                    factors.extend(prime_factor(num // i))            
                    return factors
                i += 1
            
            return [num]
                        
        
        n = pow(10, 5) + 1
        
        reps = [i for i in range(n)]
        ranks = [1] * n
        
        
        def find(member):
            root = member
            
            while reps[root] != root:
                root = reps[root]
            
            
            while reps[member] != root:
                parent = reps[member]
                reps[member] = root
                member = parent
            
            return root
            
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if xRep == yRep:
                return
            
            if ranks[xRep] > ranks[yRep]:
                reps[yRep] = xRep
                ranks[xRep] += ranks[yRep]
            
            else:
                reps[xRep] = yRep
                ranks[yRep] += ranks[xRep]
                                                            
        
        for num in nums:
            if num == 1:
                return False
            
            factors = prime_factor(num)
            
            for i in range(1, len(factors)):
                union(factors[i], factors[i - 1])
            
            if factors:
                union(factors[0], num)
        
        unique_reps = set()
        for num in nums:
            unique_reps.add(find(num))
                
        return len(unique_reps) == 1
        
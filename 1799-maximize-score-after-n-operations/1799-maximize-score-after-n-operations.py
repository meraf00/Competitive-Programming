class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length = len(nums) 
                                
        def gcd(a, b):                 
            x, y = max(a, b), min(a, b)
            
            while y > 0:
                temp = x
                x = y
                y = temp % y            
                
            return x                        
        
        
        
        @cache
        def backtrack(ops, taken):
            max_score = 0
                        
            for i in range(length):       
                if taken & (1 << i):
                    continue
                    
                for j in range(length):                    
                    if i != j and not (taken & (1 << j)):
                        taken ^= (1 << i)                    
                        taken ^= (1 << j)  
                        
                        score = ops * gcd(nums[i], nums[j])
                        
                        score += backtrack(ops + 1, taken)
                        
                        max_score = max(score, max_score)
                        
                        taken ^= (1 << i)                                        
                        taken ^= (1 << j) 
            
            return max_score
        
        return backtrack(1, 0)            
                
                
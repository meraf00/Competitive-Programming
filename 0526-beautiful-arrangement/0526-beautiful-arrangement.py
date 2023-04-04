class Solution:
    def countArrangement(self, n: int) -> int:
        
        count = 0
                
        seen = set()        
        
        def backtrack():
            nonlocal count
            
            if len(seen) == n:
                count += 1
                return
            
            for num in range(1, n + 1):
                if num in seen:
                    continue
                    
                if num % (len(seen) + 1) != 0 and (len(seen) + 1) % num != 0:
                    continue
                    
                
                seen.add(num)
                
                backtrack()
                                
                seen.discard(num)
        
        
        backtrack()
        
        return count
class Solution:
    def countArrangement(self, n: int) -> int:
        
        count = 0
                
        seen = 0           
        
        def backtrack(current_length):
            nonlocal count, seen
            
            if current_length == n:
                count += 1
                return
            
            for num in range(1, n + 1):
                if 1 << num & seen:
                    continue
                    
                if num % (current_length + 1) != 0 and (current_length + 1) % num != 0:
                    continue
                    
                
                seen ^= 1 << num
                
                backtrack(current_length + 1)
                                
                seen ^= 1 << num
        
        
        backtrack(0)
        
        return count
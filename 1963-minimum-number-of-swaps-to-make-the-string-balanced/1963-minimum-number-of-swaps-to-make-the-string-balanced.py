class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)                
        
        open_count = 0        
        swap_count = 0
        
        last_opening = n - 1
        
        for i in range(last_opening, -1, -1):
            if s[i] == '[':
                last_opening = i
                break
                
                
        for i in range(last_opening):             
            if i >= last_opening:
                break
                
            if s[i] == '[':
                open_count += 1
            
            elif open_count:
                open_count -= 1
            
            else:                                
                swap_count += 1
                open_count += 1
                
                for j in range(last_opening, i - 1, -1):
                    if s[last_opening] == '[':
                        last_opening = j
                        break                                
                
                                        
        return swap_count
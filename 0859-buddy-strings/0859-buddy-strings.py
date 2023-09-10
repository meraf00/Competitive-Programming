class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        
        last_diff = None
        error_count = 0
        
        for a, b in zip(s, goal):
            if a != b:
                error_count += 1
                
                if error_count > 2:
                    return False
                
                if not last_diff:
                    last_diff = (a, b)
                
                elif (b, a) != last_diff:
                    return False
        
        if error_count == 0:
            s_count = Counter(s)
            
            for count in s_count.values():
                if count > 1:
                    return True
                
        return error_count == 2
                    
                    
            
            
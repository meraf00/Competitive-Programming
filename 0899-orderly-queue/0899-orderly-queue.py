class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
                
        min_string = list(s)
        curr_string = list(s)
        
        length = len(s)
        
        for i in range(length):
            for j in range(length):
                curr_string[j] = s[(i + j) % length]
            
            if min_string > curr_string:
                min_string = curr_string[:]
        
        return ''.join(min_string)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        length = len(s)
        
        flipped = [float('inf')] * length
        unflipped = [float('inf')] * length
        
        flipped[0] = 1
        unflipped[0] = 0
        
        for i in range(1, length):            
            if s[i] == '1':
                unflipped[i] = min(flipped[i - 1], unflipped[i - 1])
                
                if s[i - 1] == '0':
                    flipped[i] = min(flipped[i], unflipped[i - 1]) + 1
                
                else:
                    flipped[i] = min(flipped[i], flipped[i - 1]) + 1
                                
            else:
                flipped[i] = min(flipped[i - 1], unflipped[i - 1]) + 1
                
                if s[i - 1] == '1':
                    unflipped[i] = min(unflipped[i], flipped[i - 1])
                
                else:
                    unflipped[i] = min(unflipped[i], unflipped[i - 1])

        
        return min(unflipped[-1], flipped[-1])
                
                
            
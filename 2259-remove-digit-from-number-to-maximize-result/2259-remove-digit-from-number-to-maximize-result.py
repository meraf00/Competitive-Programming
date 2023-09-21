class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        length = len(number)
        
        number += ' '
        
        last_idx = 0
        
        for i in range(1, len(number)):
            dig = number[i - 1]
            next_dig = number[i]
            
            if dig != digit:
                continue
            
            last_idx = i - 1
            
            if dig < next_dig:
                return number[:i - 1] + number[i:length]
        
        return number[:last_idx] + number[last_idx + 1:length]
        
                
                
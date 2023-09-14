class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        
        letter_count = Counter(s)                
        
        answer = []
        
        sorted_letters = sorted(set(s)) 
        sorted_letters += list(reversed(sorted_letters))
        
        k = len(sorted_letters)
        i = 0
        
        while n:
            current_letter = sorted_letters[i % k]
            
            if letter_count[current_letter] > 0:
                n -= 1
                letter_count[current_letter] -= 1
                answer.append(current_letter)
            
            i += 1
        
        return ''.join(answer)
                
            
        
        
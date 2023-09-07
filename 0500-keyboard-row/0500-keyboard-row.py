class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")            
        ]
        
        answer = []
        
        for word in words:
            chars = set(word.lower())
            n_chars = len(chars)
            
            for row in keyboard:                    
                if len(chars.intersection(row)) == n_chars:
                    answer.append(word)
                    break
            
        return answer
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        
        current_word = []
        for char in s:
            if char == " ":
                if current_word:
                    words.append("".join(current_word))
                    current_word = []
                continue
            
            current_word.append(char)
        
        if current_word:
            words.append("".join(current_word))
            
        return " ".join(reversed(words))
            
            
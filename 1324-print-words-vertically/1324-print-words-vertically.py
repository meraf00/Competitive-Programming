class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        
        max_word_length = max(map(len, words))
        
        output = []
        
        for i in range(max_word_length):
            col = []
            for word in words:
                if i < len(word):
                    col.append(word[i])
                else:
                    col.append(" ")
            output.append("".join(col).rstrip())
        
        return output    
        
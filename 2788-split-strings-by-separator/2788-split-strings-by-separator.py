class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        splited = []                
        
        for word in words:
            
            current_word = []
            
            for char in word:
                if char == separator:
                    if current_word:
                        splited.append("".join(current_word))
                        current_word = []
                    continue
            
                current_word.append(char)
            
            if current_word:
                splited.append("".join(current_word))
        
        
        return splited
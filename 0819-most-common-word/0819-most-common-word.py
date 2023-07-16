class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)                
        
        letters = set(string.ascii_letters)
        
        words = []
        word = []
        for char in paragraph.lower():        
            if char in letters:
                word.append(char)
            elif word:
                words.append("".join(word))
                word = []
        
        if word:
            words.append("".join(word))
                
        
        word_counter = defaultdict(int)        
        
        most_freq = None
        max_count = 0 
        
        for word in words:
            if word not in banned:
                word_counter[word] += 1
                
                if word_counter[word] > max_count:
                    max_count = word_counter[word]
                    most_freq = word
        
        return most_freq
                
        
        
            
        
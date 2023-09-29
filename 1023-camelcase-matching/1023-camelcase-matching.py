class Solution:        
    def is_subsequence(self, word, seq, seq_upper_count):        
        length = len(seq)
        
        i = 0
        
        word_upper_count = 0
        
        for char in word:
            if char.isupper():
                word_upper_count += 1
                
            if i < length and char == seq[i]:
                i += 1                        
        
        return i >= length and word_upper_count == seq_upper_count
            
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:        
        upper_count = 0
        
        for char in pattern:
            if char.isupper():
                upper_count += 1
        
        output = []
        
        for word in queries:            
            output.append(self.is_subsequence(word, pattern, upper_count))
        
        return output
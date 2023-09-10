class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = defaultdict(int)
        
        for word in s1.split(' '):
            counter[word] += 1
        
        for word in s2.split(' '):
            counter[word] += 1
            
        
        uncommon_words = []
        
        for word, count in counter.items():
            if count == 1:
                uncommon_words.append(word)
            
        return uncommon_words
            
        
            
            
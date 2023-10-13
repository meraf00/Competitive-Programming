class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:        
        vocab = Counter(words)
        
        n = len(words)
        
        word_length = len(words[0])
        
        window_size = word_length * n    
        
        ans = []
        
        for right in range(window_size, len(s) + 1):            
            
            current = defaultdict(int)
            
            for i in range(right - window_size, right, word_length):
                word = s[i: i + word_length]
                
                if word not in vocab:
                    break
                
                current[word] += 1                        
            
            if current == vocab:
                ans.append(right - window_size)
        
        return ans
                
    
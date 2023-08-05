class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        
        letters = []
        
        for char, freq in frequency.items():
            letters.append((freq, char))
                
        letters.sort(reverse=True)
                
        answer = []
        
        for freq, char in letters:
            answer.append(char * freq)
            
        
        return "".join(answer)
        
        
            
        
        
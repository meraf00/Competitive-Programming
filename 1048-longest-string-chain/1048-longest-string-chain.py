class Solution:
    def longestStrChain(self, words: List[str]) -> int:        
        # chain lengths ending with word
        chain_lengths = defaultdict(int)        
        
        # sorted with length
        words.sort(key=lambda word: len(word))
        
        for word in words:                            
            for idx, _ in enumerate(word):                 
                one_char_removed = word[:idx] + word[idx + 1:]                  
                
                chain_lengths[word] = max(
                    chain_lengths[one_char_removed] + 1, 
                    chain_lengths[word])
                
        
        return max(chain_lengths.values())
        
        
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = []
                
        for idx, word in enumerate(words):
            mask = 0
            for char in word:
                mask |= 1 << ord(char) - ord('a')
            
            bitmask.append(mask)
            words[idx] = len(word)
        
        n_words = len(words)
        
        max_product = 0
        
        for i in range(n_words):
            for j in range(i + 1, n_words):
                if bitmask[i] ^ bitmask[j] == bitmask[i] + bitmask[j]:
                    max_product = max(max_product, words[i] * words[j])
        
        return max_product
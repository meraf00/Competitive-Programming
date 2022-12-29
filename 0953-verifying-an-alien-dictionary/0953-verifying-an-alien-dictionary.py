class Solution:
    def areOrdered(self, word1, word2, order):        
        min_length = min(len(word1), len(word2))
        
        for i in range(min_length):
            char1 = word1[i]
            char2 = word2[i]
            
            if order[char1] < order[char2]:                
                return True
            elif order[char1] > order[char2]:
                return False
        
        if len(word1) > len(word2):
            return False
        
        return True        
        
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_ = {}
        for i, char in enumerate(order):
            order_[char] = i
            
        for i in range(len(words)-1):            
            if not self.areOrdered(words[i], words[i+1], order_):
                return False
        return True

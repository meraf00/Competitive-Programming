"""https://leetcode.com/problems/verifying-an-alien-dictionary"""

from typing import List

class AlienString:
    def __init__(self, s, order):                
        self.s = s
        self.order = order
    
    def compare(self, word1, word2):
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            char1 = word1[i]
            char2 = word2[i]
            if self.order[char1] > self.order[char2]:
                return 1
            elif self.order[char1] < self.order[char2]:
                return -1                        
        
        if len(word1) < len(word2):
            return -1
        return 1
    
    def __len__(self):
        return len(self.s)
    
    def __getitem__(self, index):
        return self.s[index]
    
    def __lt__(self, s2):
        return self.compare(self.s, s2) == -1
    
    def __gt__(self, s2):
        return self.compare(self.s, s2) == 1

class Solution:
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_ = {}
        for i, char in enumerate(order):
            order_[char] = i
                
        words = list(map(lambda word: AlienString(word, order_), words))

        for i, word in enumerate(words[1:]):
            if word < words[i]:                
                return False
            
        return True    
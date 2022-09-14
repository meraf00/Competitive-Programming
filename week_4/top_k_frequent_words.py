"""
https://leetcode.com/problems/top-k-frequent-words/
"""

import heapq
from typing import List

class Comparable:
    def __init__(self, word: str, freq:int = 1):
        self.word = word
        self.freq = freq
    
    def __lt__(self, comparable):
        if comparable.freq == self.freq:
            return self.word > comparable.word
        return self.freq < comparable.freq
    
    def __gt__(self, comparable):
        if comparable.freq == self.freq:
            return self.word < comparable.word
        return self.freq > comparable.freq
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}
        
        for word in words:
            if word_freq.get(word):
                word_freq[word].freq += 1
            else:
                word_freq[word] = Comparable(word)
        
        comparable_word_list = list(word_freq.values())
        
        heapq._heapify_max(comparable_word_list)
        
        words = []
        while k > 0:
            words.append(heapq._heappop_max(comparable_word_list).word)
            k -= 1
            
        return words
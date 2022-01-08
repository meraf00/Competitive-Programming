from typing import List

class Solution:

    def extractIndex(self, s: str) -> int:
        return int(s[-1]) - 1
        
        
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        
        indexes = map(self.extractIndex, words)
        
        answer = [""] * len(words)
        
        for i, j in enumerate(indexes):
            answer[j] = words[i][0 : -1]
        
        return " ".join(answer)

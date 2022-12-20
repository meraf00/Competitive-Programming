class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        i = j = 0
        while i < len(word1) and j < len(word2):
            output += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):
            output += word1[i:]
        if j < len(word2):
            output += word2[j:]
        
        return output


"""https://leetcode.com/problems/reverse-words-in-a-string-iii/"""

class Solution:
    # attempt 2
    def reverseWords(self, s: str) -> str:        
        return " ".join(s[::-1].split(" ")[::-1])

    # attempt 1    
    def reverseWords_(self, s: str) -> str:
        s = [c for c in s]

        word_start = 0
        word_end = 0

        while word_end < len(s):
            if s[word_end] == " " or word_end == len(s) - 1:
                temp = word_end + 1
                if word_end != len(s) - 1:
                    word_end -= 1
                while word_start < word_end:
                    s[word_start], s[word_end] = s[word_end], s[word_start]
                    word_start += 1
                    word_end -= 1                
                word_start = word_end = temp
            word_end += 1

        return "".join(s)
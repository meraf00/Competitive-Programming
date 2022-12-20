"""https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = " abcdefghijklmnopqrstuvwxyz"

        output = ""
        token = ""
        for char in s:
            if char == "#":                
                if len(token) == 2:
                    output += letters[int(token)]
                else:
                    for index in list(token[:-2]):
                        output += letters[int(index)]
                    output += letters[int(token[-2:])]
                token = ""
            else:
                token += char
        if token:
            for index in list(token):
                output += letters[int(index)]
        return output
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        pointer = 0        
        
        for char in t:
            if pointer >= len_s:
                break
                
            if char == s[pointer]:
                pointer += 1
        
        
        return pointer == len(s)
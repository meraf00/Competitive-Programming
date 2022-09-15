"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
"""

class Solution:
    def invert(self, string: str) -> str:
        inverted = [""] * len(string)
        for i, bit in enumerate(string):
            if bit == "0":
                inverted[i] = "1"
            else:
                inverted[i] = "0"
        return "".join(inverted)
    
    def str_builder(self, n: int) -> str:
        if n == 1:
            return "0"
        
        n_1 = self.str_builder(n-1)        
        return n_1 + "1" + "".join(reversed(self.invert(n_1)))
        
    def findKthBit(self, n: int, k: int) -> str:        
        return self.str_builder(n)[k - 1]
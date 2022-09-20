"""
https://leetcode.com/problems/remove-k-digits/
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            if len(stack) > 0 or digit != "0":
                stack.append(digit)
        
        while stack and k > 0:
            stack.pop()
            k -= 1
            
        return "0" if len(stack) == 0 else "".join(stack)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        
        ans = []
        
        left = 0
        
        for right, char in enumerate(s):
            if char == "(":
                stack.append(char)
            
            else:
                stack.pop()
            
            
            if not stack:
                ans.append(s[left + 1:right])
                left = right + 1
        
        return ''.join(ans)
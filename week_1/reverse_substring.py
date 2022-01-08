class Solution:
    def reverseParentheses(self, s: str) -> str: 
        
        s = list(s)
        
        stack = []
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            
            elif char == ")":
                begin = stack.pop() + 1
                
                for k, ch in enumerate(reversed(s[begin : i])):
                    s[begin + k] = ch
        
        return "".join(s).replace("(", "").replace(")", "")
                

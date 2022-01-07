class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for b in s:
            if b in ["(", "[", "{"]:
                stack.append(b)
                
            elif b in [")", "]", "}"]:
                if stack and (stack[-1] == "(" and b == ")"  or stack[-1] == "[" and b == "]" or stack[-1] == "{" and b == "}"):
                        stack.pop()                    
                else:
                    return False
                
        if stack:
            return False
        else:
            return True
       
        
        

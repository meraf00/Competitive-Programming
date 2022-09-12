"""
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:        
    def calculate(self, s: str) -> int: 
        
        stack = []
        
        current = 0
        operator = "+"
        
        i = 0
        while i < len(s):            
            if s[i] == " ": 
                i += 1
                continue
            
            elif s[i] not in "+-*/":
                while i < len(s) and s[i].isdigit():
                    current = current * 10 + int(s[i])   
                    i += 1          
                                
                if operator == "-":
                    stack.append(-1 * current)
                elif operator == "*":
                    stack.append(stack.pop() * current)
                elif operator == "/":                    
                    stack.append(int(stack.pop()/ current))
                else:
                    stack.append(current)
                current = 0
                continue
            else:
                operator = s[i]                        
            
            i += 1
        
        return sum(stack)    
        
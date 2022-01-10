from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:            
            if t not in ["+", "-", "*", "/"]:            
                stack.append(int(t))
            else:       
                num2, num1 = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                elif t == "/":
                    stack.append(int(num1 / num2))
        
        return stack[0]

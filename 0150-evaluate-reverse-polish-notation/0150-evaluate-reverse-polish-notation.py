class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b,
            "*": lambda a, b : a * b,
            "/": lambda a, b : int(a / b)
        }
        
        stack = []
        
        for token in tokens:
            
            if token in ops:                
                b = int(stack.pop())
                a = int(stack.pop())
                
                operation = ops[token]
                
                result = operation(a, b)
                                
                stack.append(result)
                
                continue
            
            stack.append(int(token))
        
        return stack[-1]
        
        
        
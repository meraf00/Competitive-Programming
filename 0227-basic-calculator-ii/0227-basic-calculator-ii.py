class Solution:    
    def calculate(self, s: str) -> int:
        parsed = self.parse(s)
        
        stack = []                
        
        prev = None
        operation = None
                
        for token in parsed:                        
            if type(token) == int:   
                if operation == '*':
                    stack.append(prev * token)
                
                elif operation == '/':
                    stack.append(int(prev / token))
                
                else:
                    stack.append(token)
                
                operation = prev = None
            
            if token == '*':
                prev = stack.pop()
                operation = '*'
            
            elif token == '/':
                prev = stack.pop()
                operation = '/'                        
                
        
        return sum(stack)
    
    def parse(self, s):
        parsed = []
        
        number = 0
        
        for char in s:
            if char == ' ':
                continue
                
            elif char.isdigit():
                number *= 10
                number += int(char)
            
            else:    
                if parsed and parsed[-1] == '-':
                    parsed.pop()
                    parsed.append(-1 * number)
                
                else:
                    parsed.append(number)
                    
                parsed.append(char)
                number = 0
        
        if parsed and parsed[-1] == '-':
            parsed.pop()
            parsed.append(-1 * number)

        else:
            parsed.append(number)
        
        return parsed
                
                
        
        
            
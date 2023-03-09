class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == "()":
            return 1
        
        
        stack = []                
        
        
        scores = 0
        
        for index, char in enumerate(s):
            if char == "(":                                
                stack.append(index)
            
            else:
                start_index = stack.pop()                                                
                
                if not stack: 
                    if index - start_index == 1:
                        scores += 1
                    else:
                        scores += 2 * self.scoreOfParentheses(s[start_index + 1 : index])
        
        return int(scores)
            
            
                
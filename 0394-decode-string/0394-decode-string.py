class Solution:
    letters = set("abcdefghijklmnopqrstuvwxyz")
    nums = set("1234567890")  
    brackets = set("[]")
    
    def typeof(self, char):
        if char in self.letters:
            return 0
        elif char in self.nums:
            return 1
        else:
            return 2
        
    def tokenize(self, s):
        tokens = []        
        
        right = 0
        while right < len(s):
            
            if s[right] in self.brackets:
                tokens.append(s[right])
                right += 1
                continue
                                    
            current = [s[right]]            
            
            right += 1
                        
            
            while right < len(s) and self.typeof(s[right]) == self.typeof(current[-1]):
                current.append(s[right])
                right += 1
            
            token = "".join(current)
            
            tokens.append(token)                        
        
        return tokens 
    
    def decode(self, tokens):
        stack = []
        
        bracket_count = 0
        
        for index, token in enumerate(tokens):
            if token == "[":
                bracket_count += 1
                stack.append(index)
            
            elif token == "]":                
                start = stack.pop()
                end = index
                
                # how many times to repeat the string is specified before opening bracket
                count = int(tokens[start - 1])
                
                # repeat the enclosed string count times and update the token
                encoded = "".join(tokens[start + 1 : end]) 
                
                new_tokens = tokens[:start-1] + [encoded * count] + tokens[end + 1:]  
                break
                
        if bracket_count > 0:            
            return self.decode(new_tokens)
            
        return [token for token in tokens if not token.isdigit()]
        
        
            
    def decodeString(self, s: str) -> str:
        
        tokens = self.tokenize(s)
        
        decoded = self.decode(tokens)
                        
        return "".join(decoded)
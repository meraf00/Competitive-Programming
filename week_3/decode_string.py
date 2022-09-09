from typing import List

class Solution:
            
    def decodeString(self, s: str) -> str:        
        stack = []
        
        s = list(s)
        
        i = 0
        while i < len(s):            
            if s[i] == "[":
                j = i - 1                
                while j > -1 and s[j].isdigit():                    
                    j -=  1
                
                j += 1
                repeat = int("".join(s[j:i]))
                new = s[0:j]                 
                new.extend(s[i + 1:])
                s = new                
                i = j
                stack.append((j, repeat))
            
            elif s[i] == "]":
                index, repeat = stack.pop()                  
                s[index] = "".join(s[index:i]) * repeat                                                
                del s[index+1 : i+1]
                i = index
                continue
                            
            i += 1
        
        return "".join(s)
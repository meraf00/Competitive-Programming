
class Solution:
    def __init__(self):
        self.flag = False
    
    
    def backtrack(self, splitted, string):
        if len(string) == 0 and len(splitted) > 1:
            self.flag = True
        
        
        if self.flag:
            return
        
        
        for index in range(len(string)):
            new_splitted = splitted[:]
            
            
            next_num = int(string[:index + 1])
            
            if new_splitted:
                if new_splitted[-1] - next_num == 1:
                    new_splitted.append(next_num)
                
                else:
                    continue
                        
            else:
                new_splitted.append(next_num)
            
            
            self.backtrack(new_splitted, string[index + 1:])
       
    
    def splitString(self, s: str) -> bool:
        
        self.backtrack([], s)
        
        return self.flag
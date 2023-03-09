class Solution:
    def splitString(self, s: str) -> bool:
        flag = False
        
        def backtrack(built_, s_):
            nonlocal flag
           
            if len(s_) == 0 and len(built_) > 1:
                flag = True
            
            if flag:                
                return
            
            # print(">", built_, s_)

            for i in range(len(s_)):
                built = built_[:]         
                
                if built:                    
                    if built[-1] - int(s_[:i + 1]) == 1:
                        built.append(int(s_[:i + 1]))
                    
                    else:
                        continue
                    
                        
                else:
                    
                    built.append(int(s_[ : i+1]))
                                
                backtrack(built, s_[i + 1:])                                            
                
            
        
        backtrack([], s)
        
        return flag
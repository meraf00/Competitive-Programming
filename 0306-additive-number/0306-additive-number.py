class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)        
        
        current = []        
        
        def backtrack(start_index):

            if start_index >= length:
                if len(current) < 3:
                    return False
                
                
                for i in range(len(current) - 2):
                    if current[i] + current[i + 1] != current[i + 2]:
                        return False 
                    
                return True
        
            if len(current) >= 3 and current[-1] != current[-2] + current[-3]:
                return False                            
            
            for i in range(start_index, length):
                next_num = num[start_index : i + 1]
                
                if int(next_num) > 0 and next_num[0] == "0":
                    return False
                
                next_num = int(next_num)
                
                current.append(next_num)
                
                if backtrack(i + 1):
                    return True
                
                current.pop()
            
            return False
        
        
        return backtrack(0)
                
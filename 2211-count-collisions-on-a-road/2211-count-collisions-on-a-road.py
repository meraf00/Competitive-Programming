class Solution:
    def countCollisions(self, directions: str) -> int:
        state = []
        
        count = 0
        
        for car in directions:
            if not state:
                state.append(car)
            
            elif state[-1] == 'R' and car == 'L':                
                while state and state[-1] == 'R':
                    state.pop()
                    count += 1 
                count += 1
                state.append('S')
                
            
            elif state[-1] == 'S' and car == 'L':
                count += 1                            
            
            elif state[-1] == 'R' and car == 'S':                
                while state and state[-1] == 'R':
                    state.pop()
                    count += 1                 
                state.append('S')          
            
            else:
                state.append(car)    
                        
        
        return count
            
'''
"RLRSLL"
"LLRR"
"RL"
"LR"
"SSS"
"S"
"L"
"R"
"RLLR"
"SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
'''         
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        soln = [0] * len(temperatures)
                
        for i in range(len(temperatures)):
            # new temp > last temp
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                soln[index] = i - index
            
            stack.append(i)                                    
        return soln
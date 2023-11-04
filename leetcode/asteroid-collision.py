class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for weight in asteroids:               
            if not stack or weight > 0:
                stack.append(weight)                
                continue                            
            
            append = True
            
            while stack and stack[-1] > 0:                                 
                if stack[-1] < -weight:
                    stack.pop()
                
                elif stack[-1] > -weight: 
                    append = False
                    break
                
                else:
                    append = False
                    stack.pop()                    
                    break
                
            if append:
                stack.append(weight)            
                            
        return stack
                
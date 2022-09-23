"""
https://leetcode.com/problems/min-stack/
"""

class MinStack:
    
    def __init__(self):
        self.stack = [] 
        self.min_stack = []

    def push(self, val: int) -> None:   
        if not self.stack or (self.stack and self.min_stack[-1] >= val):
            self.min_stack.append(val)
            
        self.stack.append(val)

    def pop(self) -> None:  
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
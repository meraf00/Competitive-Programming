class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x: int) -> None:          
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())
        
        self.stack_1.append(x)
        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())
            
        

    def pop(self) -> int:
        return self.stack_1.pop()        
        

    def peek(self) -> int:
        value  = self.stack_1.pop()
        self.stack_1.append(value)
        return value

    def empty(self) -> bool:
        return not bool(len(self.stack_1))
        


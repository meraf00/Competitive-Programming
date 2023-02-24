class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.back = 0
        self.size = k
        self.element_count = 0
        

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        self.queue[self.back] = value     
        self.back = (self.back + 1) % self.size        
        self.element_count += 1
        
        return True
    

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
               
        self.front = (self.front + 1) % self.size
        self.element_count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]
        

    def Rear(self) -> int:        
        if self.isEmpty():
            return -1
        
        return self.queue[(self.back - 1) % self.size]
        

    def isEmpty(self) -> bool:
        return self.element_count == 0
        

    def isFull(self) -> bool:
        return self.element_count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
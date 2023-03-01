class Node:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node()
        
        self.tail = self.head
        self.head.next = self.head
        self.head.prev = self.head
        
        self.count = 0
        self.capacity = k                
    
    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.head.value = value
            self.count += 1
            
            return True
        
        if self.isFull():
            return False
        
        new_node = Node(value, self.tail, self.head)
        
        self.head.prev = new_node
        
        self.tail.next = new_node                
        
        self.head = new_node
        
        self.count += 1  
        
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.head.value = value
            self.count += 1            
            return True
        
        if self.isFull():
            return False
        
        new_node = Node(value, self.tail, self.head)
        
        self.head.prev = new_node
        
        self.tail.next = new_node
        
        self.tail = new_node
        
        self.count += 1        
        
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.head.prev = self.tail
        
        self.tail.next = self.head        
        
        self.count -= 1
        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False  
                        
        self.head.prev = self.tail.prev
        
        self.tail.prev.next = self.head
        
        self.tail = self.tail.prev
                        
        self.count -= 1
                
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.value

    def isEmpty(self) -> bool:        
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
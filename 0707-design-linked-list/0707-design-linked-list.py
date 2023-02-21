class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1
            
        return current.val       

    def addAtHead(self, val: int) -> None:        
        new_node = Node(val)
        
        if self.head:              
            new_node.next = self.head
            self.head.prev = new_node
            
            if self.length == 1:
                self.tail = self.head
            
            self.head = new_node
            
        else:
            self.head = self.tail = new_node
        self.length += 1
            

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head:            
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node            
        else:
            self.head = self.tail = new_node
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1
        
        new_node = Node(val)
        current.prev.next = new_node
        new_node.prev = current.prev
        new_node.next = current
        current.prev = new_node        
        
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1
        
        if index == self.length - 1: # tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:                
                self.tail = self.tail.prev
                self.tail.next = None
        elif index == 0:    # head
            self.head = self.head.next
            self.head.prev = None
        else:                        
            current.prev.next = current.next
            current.next.prev = current.prev
            
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
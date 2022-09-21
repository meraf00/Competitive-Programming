"""
https://leetcode.com/problems/lru-cache/
"""


class Node:
    def __init__(self, value: int, key: int):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_front(self, node: Node):        
        if self.head:            
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.size += 1
    
    def remove(self, node: Node):
        if node == self.head == self.tail:
            self.head = self.tail = None            
        
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None            
        
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:            
            node.prev.next = node.next            
            node.next.prev = node.prev
        
        self.size -= 1
            
        node.prev = None
        node.next = None
    
    def move_to_front(self, node: Node):
        if node == self.head:
            return        
        
        self.remove(node)
        
        self.add_front(node)
    
    def __len__(self):
        return self.size
            

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = LinkedList()
        self.hashmap = {}
        

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        if node:
            self.queue.move_to_front(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.hashmap.get(key)
        if node:
            node.value = value
            self.queue.move_to_front(node)            
        
        else:
            node = Node(value, key)
            self.queue.add_front(node)
            
            self.hashmap[key] = node
                    
        if self.queue.size > self.capacity:
            del self.hashmap[self.queue.tail.key]
            self.queue.remove(self.queue.tail)            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
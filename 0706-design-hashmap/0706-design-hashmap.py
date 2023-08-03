class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: 'Node' = None
    
    def __repr__(self):
        return f"{(self.key, self.value)} -> {self.next}"

class MyHashMap:

    def __init__(self):
        self._size = 10 ** 4
        self._map = [None] * self._size
    
    def _get_node(self, key: int) -> int:        
        idx = key % self._size
        
        current = self._map[idx]
        while current and current.key != key:
            current = current.next                
        
        return current
        

    def put(self, key: int, value: int) -> None:  
        # print(self._map)
        # if key already exists, update
        node = self._get_node(key)
        if node:
            node.value = value
            return
                        
        idx = key % self._size
        
        if self._map[idx] == None:
            self._map[idx] = Node(key, value)
        
        else:
            head = Node(key, value)
            head.next = self._map[idx]
            self._map[idx] = head                

    def get(self, key: int) -> int:  
        # print(self._map)
        node = self._get_node(key)
        
        if not node:
            return -1
        
        return node.value
        

    def remove(self, key: int) -> None: 
        # print(self._map)
        idx = key % self._size
        
        prev = None
        current = self._map[idx]
        while current and current.key != key:
            prev = current
            current = current.next
        
        if current:
            if prev:
                prev.next = current.next
            
            else:
                self._map[idx] = current.next
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
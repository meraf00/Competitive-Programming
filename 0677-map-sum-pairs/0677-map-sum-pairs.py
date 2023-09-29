class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = 0
        

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
        
        current.value = val
        
        current.is_end = True
                        
    def sum(self, prefix: str) -> int:
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return 0
        
            current = current.children[char]
        
        stack = [current]
        
        value_sum = 0
        
        while stack:
            node = stack.pop()
            
            if node.is_end:
                value_sum += node.value
                                        
            for child in node.children.values():                
                stack.append(child)
                
        return value_sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
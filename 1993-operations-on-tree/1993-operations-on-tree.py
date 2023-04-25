class LockingTree:

    def __init__(self, parent: List[int]):
        self.tree = defaultdict(list)
        
        for node, parent_node in enumerate(parent):
            if parent_node == -1:
                continue
                
            self.tree[parent_node].append(node)
        
        self.parent = parent
        
        self.locked = {}
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) == user:
            del self.locked[num]
            return True
        
        return False
    
    def has_locked_descendant(self, node):            
        has_locked = node in self.locked
        
        if node in self.locked:
            del self.locked[node]
            
        for nbr in self.tree[node]:
            has_locked = self.has_locked_descendant(nbr) or has_locked
        
        return has_locked

    def upgrade(self, num: int, user: int) -> bool:   
        # Rule #1
        if num in self.locked:
            return False                        
                
        
        # Rule #3
        ancestor = self.parent[num]
        
        while ancestor != -1:                  
            # found locked ancestor
            if ancestor in self.locked:                
                return False
            
            ancestor = self.parent[ancestor]
        
        
        # Rule #2
        if self.has_locked_descendant(num):
            self.locked[num] = user
            return True
        
        return False
        
        
        
        
            
        

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
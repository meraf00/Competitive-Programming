class UnionFind:
    def __init__(self, n):
        self.rep  = {i: i for i in range(n)}
        self.self.rank = {i: 1 for i in range(n)}
        
        
    def find(self, node):
        current = node
        while current != self.rep[current]:
            current = self.rep[current]
        
        while node != self.rep[node]:
            temp = self.rep[node]
            self.rep[node] = current
            node = temp
        
        return current
        
        
    def union(self, a, b):
        repA = self.find(a)
        repB = self.find(b)
        
        if self.rank[repA] >= self.rank[repB]:
            self.rep[repB] = repA
            self.rank[repA] += self.rank[repB]
        
        else:
            self.rep[repA] = repB
            self.rank[repB] += self.rank[repA]
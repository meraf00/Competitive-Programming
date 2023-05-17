class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
                
        rep  = [i for i in range(n)]
        rank = [1] * n
        
        
        def find(node):
            current = node
            while current != rep[current]:
                current = rep[current]
            
            while node != rep[node]:
                temp = rep[node]
                rep[node] = current
                node = temp
            
            return current
        
        
        def union(a, b):
            repA = find(a)
            repB = find(b)
            
            if rank[repA] >= rank[repB]:
                rep[repB] = repA
                rank[repA] += rank[repB]
            
            else:
                rep[repA] = repB
                rank[repB] += rank[repA]
            
        
        for a, b in edges:
            union(a, b)        
            
        
        return find(source) == find(destination)
            
            
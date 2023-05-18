class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        rep = {i:i for i in range(1, n + 1)}
        rank = [1] * (n + 1)
        
        def find(node):
            parent = node
            while parent != rep[parent]:
                parent = rep[parent]
            
            
            while node != rep[node]:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
        
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if xRep == yRep:
                return True
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
        
        for a, b in edges:
            if union(a, b):
                return [a, b]
                
        
        
                
                
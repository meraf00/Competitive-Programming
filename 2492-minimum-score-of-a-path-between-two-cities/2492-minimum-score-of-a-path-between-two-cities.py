class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:                
        rep = {i:i for i in range(1, n + 1)}
        rep_cost = {i: float("inf") for i in range(1, n+1)}
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
                
        
        def union(x, y, cost):                                
            xRep = find(x)
            yRep = find(y)
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rep_cost[xRep] = min(rep_cost[xRep], cost)
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rep_cost[yRep] = min(rep_cost[yRep], cost)
                rank[yRep] += rank[xRep]
        
        
        for a, b, cost in roads:
            union(a, b, cost)
        
        
        rep_of_city_1 = find(1)
        
        min_path = float("inf")
        
        for city, cost in rep_cost.items():
            if find(city) == rep_of_city_1:
                min_path = min(min_path, cost)
        
        return min_path
                
        
        
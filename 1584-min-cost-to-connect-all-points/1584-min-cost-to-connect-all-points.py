class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n_points = len(points)
        
        rep = {i : i for i in range(n_points)}
        
        rank = [1] * n_points
        
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
            
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
        
        
        edges = []
        
        for pt0 in range(n_points):
            
            x0, y0 =  points[pt0]
            
            for pt1 in range(pt0 + 1, n_points):
                
                x1, y1 = points[pt1]
                
                cost = abs(x0 - x1) + abs(y0 - y1)
                
                edges.append((cost, pt0, pt1))
        
        heapify(edges)
        
        
        total_cost = 0
        
        while n_points - 1 > 0:        
            cost, pt0, pt1 = heappop(edges)
            
            if find(pt0) != find(pt1):
                total_cost += cost
                
                union(pt0, pt1)
            
                n_points -= 1
        
        
        return total_cost
        
        
                
                
                
                
            
        
            
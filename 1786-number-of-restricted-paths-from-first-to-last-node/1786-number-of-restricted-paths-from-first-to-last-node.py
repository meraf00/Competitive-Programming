class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        
        graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))        
        
        priority_queue = [(0, n - 1)]
                
        distance = [float('inf')] * n
        distance[n - 1] = 0
        
        while priority_queue:
            dist, node = heappop(priority_queue)            
                        
            for nbr, w in graph[node]:
                if distance[nbr] > dist + w:
                    distance[nbr] = dist + w
                    heappush(priority_queue, (dist + w, nbr))   
                    
        
        order = [i for i in range(1, n)]
        order.sort(key=lambda node: -distance[node])
                
        path_count = [0] * n        
        path_count[0] = 1
        
        for i in order:
            for nbr, w in graph[i]:
                if distance[nbr] > distance[i]:
                    path_count[i] = (path_count[i] % mod + path_count[nbr] % mod) % mod
                            
        return path_count[-1]
                    
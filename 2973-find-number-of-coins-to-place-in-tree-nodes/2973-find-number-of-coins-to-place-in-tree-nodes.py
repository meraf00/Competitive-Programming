class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        visited = set()
        
        coins = [0] * len(graph)
                        
        def dfs(node):                        
            visited.add(node)
            
            minheap = []
            maxheap = []
            
            for nbr in graph[node]:
                if nbr not in visited:
                    minh, maxh = dfs(nbr)
                    for value in minh:
                        heappush(minheap, value)

                        while len(minheap) > 3:
                            heappop(minheap)
                    
                    for value in maxh:
                        heappush(maxheap, value)

                        while len(maxheap) > 2:
                            heappop(maxheap)
            
            heappush(minheap, cost[node])

            while len(minheap) > 3:
                heappop(minheap)
            
            heappush(maxheap, -cost[node])

            while len(maxheap) > 2:
                heappop(maxheap)
                
            if len(minheap) < 3:
                coins[node] = 1
            
            else:                
                product = max(
                    minheap[0] * minheap[1] * minheap[2],
                    maxheap[0] * maxheap[1] * max(minheap)
                )
                if product > 0:                                    
                    coins[node] = product
            
            return minheap, maxheap
        
        dfs(0)
        
        return coins
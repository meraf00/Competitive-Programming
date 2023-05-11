class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        graph = defaultdict(list)
        
        degree = defaultdict(int)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            degree[a] += 1
            degree[b] += 1                    
                    
        queue = deque()
        
        for node in range(n):
            # leaf nodes
            if degree[node] <= 1:
                queue.append(node)
        
        
        order = []                
        
        while queue:
            current = queue.popleft()
            
            order.append(current)
            
            for nbr in graph[current]:
                degree[nbr] -= 1
                
                if degree[nbr] == 1:
                    queue.append(nbr)                
        
        
        # once we found the order we need to find what the longest distance
        # is between leaf nodes
        # Start dfs from the last node(the node we are sure will be included
        # in the answer)
        # then and find the 2 longest distances from it to leaf nodes
        # the sum of the distances is the longest distance in the graph between
        # leaf nodes                
                        
        def dfs(node, parent):
            if len(graph[node]) == 1:
                return 0                        
            
            max_depth = float('-inf')
            
            depths = []
            
            for nbr in graph[node]:
                if nbr == parent:
                    continue
                
                child_depth = dfs(nbr, node)
                
                # if we are at the root we want top 2 distances
                if parent == None:
                    
                    heappush(depths, child_depth)
                    
                    if len(depths) > 2:
                        heappop(depths)
                
                # on other nodes we want the max depth
                else:
                    max_depth = max(max_depth, child_depth)
            
            if parent == None:
                return depths
            
            return max_depth + 1
                    
        longest_distances = dfs(order[-1], None)                
        
        
        longest_distance = -sum(longest_distances) + 1
        
        # if longest distance is even it has 2 MHT
        if longest_distance & 1:
            return [order[-1]]        
        
        # if longest distance is odd it has 1 MHT
        return order[-2:]
        

class Solution:  
    def build_path(self, parent, start):
        path = set([start])
        
        while start in parent:
            path.add(parent[start])
            start = parent[start]
        
        return path
            
        
    def find_path(self, graph, start, end):
        stack = [start]
        
        parent = {}
        
        visited = set()
        
        while stack:
            current = stack.pop()
            
            visited.add(current)
            
            if current == end:
                return self.build_path(parent, end)
            
            for nbr in graph[current]:
                if nbr not in visited:
                    stack.append(nbr)
                    parent[nbr] = current
        
        return visited
        
        
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # the tree
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        freq = defaultdict(int)
        
        for start, end in trips:
            path = self.find_path(graph, start, end)
            
            for node in path:
                freq[node] += 1                
        
        @cache
        def dp(node, parent, half):
            if half:
                cost = price[node] * freq[node]

                for nbr in graph[node]:
                    if nbr == parent:
                        continue

                    cost += dp(nbr, node, False)
                
                return cost
            else:
                cost1 = price[node] * freq[node]
                cost2 = price[node] * freq[node] // 2
                
                for nbr in graph[node]:
                    if nbr == parent:
                        continue

                    cost1 += dp(nbr, node, False)
                    cost2 += dp(nbr, node, True)
                
                return min(cost1, cost2)
            
        root = trips[0][0]
        ans = dp(0, None, False)
        
        return ans
        
        
        
"""
4
[[0,1],[1,2],[1,3]]
[2,2,10,6]
[[0,3],[2,1],[2,3]]
2
[[0,1]]
[2,2]
[[0,0]]
3
[[0,1],[0,2]]
[2,4,6]
[[0,0], [0,1],[0,2]]
3
[[0,1], [0,2]]
[2,4,6]
[[0,0], [0,1]]
"""        
        
        
        
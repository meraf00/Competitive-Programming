class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        WHITE = 0 # unvisited
        BLACK = 1 # visited
        
        ancestors = [set() for _ in range(n)]
        
        indegrees = [0] * n
        
        graph = defaultdict(list)
        
        colors = [WHITE] * n
        
        for from_, to in edges:
            graph[to].append(from_)            
            ancestors[to].add(from_)
            indegrees[from_] += 1
            
        
        def topological_sort(node):            
                        
            for nbr in graph[node]:
                if colors[node] == BLACK:
                    ancestors[node].update(ancestors[nbr])
                else:
                    ancestors[node].update(topological_sort(nbr))
            
            colors[node] = BLACK
            
            return ancestors[node]
            
        for node in range(n):
            if indegrees[node] == 0:
                topological_sort(node)
        
        for i in range(n):
            ancestors[i] = sorted(ancestors[i])
    
        return ancestors
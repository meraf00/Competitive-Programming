class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        UNVISITED = 0
        WHITE = -1                
        
        colors = [UNVISITED] * len(graph)
        
        for node, state in enumerate(colors):
            if state != UNVISITED:
                continue
        
            queue = deque([node])    
            colors[node] = WHITE

            while queue:
                current = queue.popleft()

                for nbr in graph[current]:
                    if colors[nbr] == colors[current]:
                        return False

                    if colors[nbr] == UNVISITED:
                        colors[nbr] = -1 * colors[current]
                        queue.append(nbr)

        return True
                    
                    
            
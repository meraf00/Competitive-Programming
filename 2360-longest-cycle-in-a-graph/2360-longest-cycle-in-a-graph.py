class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        WHITE = 0
        GRAY  = 1
        BLACK = 2
        
        colors = [WHITE for _ in edges]
        
        longest_cycle = -1
        
        path = {}
        
        def dfs(node, distance):
            if node == -1:
                return
            
            nonlocal longest_cycle                        
            
            # cycle
            if colors[node] == GRAY:
                longest_cycle = max(longest_cycle, distance - path[node])
                colors[node] = BLACK
                return True
        
            if colors[node] == BLACK:
                return
            
            colors[node] = GRAY
            
            path[node] = distance
            
            dfs(edges[node], distance + 1)
                            
            colors[node] = BLACK
                        
        
        
        for node, color in enumerate(colors):            
            if colors[node] == WHITE:
                dfs(node, 0)
            
        return longest_cycle
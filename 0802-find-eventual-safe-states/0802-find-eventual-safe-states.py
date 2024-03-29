class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE = 0   # unvisited
        GRAY  = 1   # visited in current path 
        BLACK = 2   # visited in other path
        
        n_nodes = len(graph)
        colors = [WHITE] * n_nodes
        
        def top_sort(node):               
            if colors[node] == GRAY:
                return False
            
            if colors[node] == BLACK:
                return True
            
            colors[node] = GRAY                        
            
            for nbr in graph[node]:                
                if not top_sort(nbr):                        
                    return False
            
            colors[node] = BLACK
            return True
            
                                    
        safe_nodes = []
        
        for node in range(n_nodes):
            if top_sort(node):                
                safe_nodes.append(node)
        
        return safe_nodes
                    
        
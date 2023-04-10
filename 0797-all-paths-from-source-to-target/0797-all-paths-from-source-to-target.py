class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        
        paths = []
        
        path = [0]
        
        def dfs(current):
            if current == target:
                paths.append(path[:])
            
            for neighbour in graph[current]:
                path.append(neighbour)
                
                dfs(neighbour)
                
                path.pop()
                
            
        
        dfs(0)
        
        return paths
        
            
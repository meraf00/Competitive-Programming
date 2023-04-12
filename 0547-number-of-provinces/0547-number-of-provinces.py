class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if row == col and row not in graph:
                    graph[row] = set()
                    
                    
                if isConnected[row][col]:
                    graph[row].add(col)
        
        
        visited = set()
        
        def dfs(node):
            stack = [node]
            
            while stack:
                current = stack.pop()
                
                visited.add(current)
                
                for nbr in graph[current]:
                    if nbr not in visited:
                        stack.append(nbr)
                                
        
        provinces = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                provinces += 1
    
        return provinces
                
            
                    
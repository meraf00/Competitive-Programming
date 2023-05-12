class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        
        stack = []
        for node in graph.keys():
            if len(graph[node]) == 1:
                stack.append(node)
                break
        
        array = []  
        
        visited = set(stack)
        
        while stack:
            current = stack.pop()
            
            array.append(current)
                        
            for nbr in graph[current]:
                if nbr not in visited:
                    visited.add(nbr)
                    stack.append(nbr)
    
        return array
        
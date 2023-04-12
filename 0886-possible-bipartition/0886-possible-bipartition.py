class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # dislikes - edge list
        # build graph make it zero indexed
        
        graph = defaultdict(list)
        
        for node1, node2 in dislikes:
            graph[node1 - 1].append(node2 - 1)
            graph[node2 - 1].append(node1 - 1)
        
        
        # check bipartition                                               
        NOT_VISITED = 0
        GROUP_1 = 1
        GROUP_2 = -1 * GROUP_1
        
        color = [NOT_VISITED] * n
        
        
        for node, status in enumerate(color):
            # already visited
            if status != NOT_VISITED:                
                continue
                
            stack = [node] 
            color[node] = GROUP_1
            
            while stack:
                current = stack.pop()                                
            
                for neighbour in graph[current]:
                    # separate neighbours since they hate eachother
                    if color[neighbour] == NOT_VISITED:
                        stack.append(neighbour) 
                        color[neighbour] = -1 * color[current]
                    
                    
                    # neighbours hate eachother, are assigned to same group
                    elif color[neighbour] == color[current]:
                        return False
                            
        return True
                    
                    
                    
                    
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        
        graph = defaultdict(list)
        
        for i, bomb in enumerate(bombs):
            bomb[-1] *= bomb[-1]
                        
        for i in range(n):
            bomb_ix, bomb_iy, bomb_ir = bombs[i]
            
            for j in range(i + 1, n):        
                bomb_jx, bomb_jy, bomb_jr = bombs[j]
                
                gap = (bomb_ix - bomb_jx) ** 2 + (bomb_iy - bomb_jy) ** 2
                
                if gap <= bomb_ir:
                    graph[i].append(j)
                
                if gap <= bomb_jr:
                    graph[j].append(i)
        
        max_detonated = 0
        
        for i in range(n):
            stack = [i]
            
            visited = set()
            
            while stack:
                node = stack.pop()
                
                visited.add(node)
                
                for nbr in graph[node]:
                    if nbr not in visited:
                        stack.append(nbr)
            
            max_detonated = max(max_detonated, len(visited))
        
        return max_detonated
        
        
        
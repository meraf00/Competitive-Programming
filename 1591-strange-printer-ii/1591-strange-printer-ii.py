class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
                                            #top, right, btm, left         
        color_bounds = defaultdict(lambda : [inf,-inf,-inf,inf])
        
        
        rows = len(targetGrid)
        cols = len(targetGrid[0])
        
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]                
                color_bounds[color][0] = min(r, color_bounds[color][0])
                color_bounds[color][1] = max(c, color_bounds[color][1])
                color_bounds[color][2] = max(r, color_bounds[color][2])
                color_bounds[color][3] = min(c, color_bounds[color][3])
        
        
        graph = defaultdict(set)        
        indegree = defaultdict(int)
        
        for r in range(rows):
            for c in range(cols):
                curr_color = targetGrid[r][c]
                
                for prev_color, bounds in color_bounds.items():
                    if prev_color == curr_color:
                        continue
                        
                    top, right, btm, left = bounds
                    
                    if top <= r <= btm and left <= c <= right:
                        if curr_color not in graph[prev_color]:
                            indegree[curr_color] += 1
                            
                        graph[prev_color].add(curr_color)
        
        
        queue = deque()
        
        for color in range(1, 61):
            if indegree[color] == 0:
                queue.append(color)
        
        
        order = []
        
        while queue:
            node = queue.popleft()
            
            order.append(node)
            
            for nbr in graph[node]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)

        return len(order) == 60
                    
                    
            
                
        
        
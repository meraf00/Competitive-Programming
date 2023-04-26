class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        RED = 0
        BLUE = 1
        
        graph = defaultdict(lambda : [[], []])
        
        for src, dest in redEdges:
            graph[src][RED].append(dest)
            
        for src, dest in blueEdges:
            graph[src][BLUE].append(dest)
        
        
        ans = [float("inf")] * n
        
        # (node, color, distance)
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        
        visited_blue = set([0])
        visited_red = set([0])                
        
        while queue:
            node, color, distance = queue.popleft()
            
            ans[node] = min(ans[node], distance)
            
            if color == RED:
                for nbr in graph[node][BLUE]:
                    if nbr not in visited_blue:
                        visited_blue.add(nbr)
                        queue.append((nbr, BLUE, distance + 1))
            
            else:                
                for nbr in graph[node][RED]:
                    if nbr not in visited_red:
                        visited_red.add(nbr)                                         
                        queue.append((nbr, RED, distance + 1))
        
        for i in range(n):
            if ans[i] == float("inf"):
                ans[i] = -1
                
        return ans
        
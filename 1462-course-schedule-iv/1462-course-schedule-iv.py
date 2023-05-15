class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        
        def bfs(start):
            queue = deque([start])
            
            visited = set([start])
        
            while queue:
                current = queue.popleft()
                
                isPrereq[start][current] = True
                
                for nbr in graph[current]:                                        
                    if nbr not in visited:
                        isPrereq[current][nbr] = True
                        queue.append(nbr)
                        visited.add(nbr)
                    
        
        answer = []
        for a, b in queries:
            if isPrereq[a][b] == -1:
                bfs(a)
                if isPrereq[a][b] == -1:
                    isPrereq[a][b] = False
                answer.append(isPrereq[a][b])
            else:
                answer.append(isPrereq[a][b])
        
        return answer
            
                
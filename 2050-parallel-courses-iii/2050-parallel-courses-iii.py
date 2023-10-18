class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        
        indegree = [0] * n
        
        for prereq, course in relations:
            graph[prereq - 1].append(course - 1)
        
            indegree[course - 1] += 1
        
        queue = deque()
        
        required_months = [0] * n
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                required_months[i] = time[i]
        
        while queue:
            node = queue.popleft()
            
            for nbr in graph[node]:
                indegree[nbr] -= 1
                
                required_months[nbr] = max(required_months[node] + time[nbr], required_months[nbr])
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return max(required_months)
        
            
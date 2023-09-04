class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        
        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        
        order = []
        
        while queue:
            course = queue.popleft()
                        
            order.append(course)
            
            for nbr in graph[course]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        if len(order) < numCourses:
            return []
        
        return order
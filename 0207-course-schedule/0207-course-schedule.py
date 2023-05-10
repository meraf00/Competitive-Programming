class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        indegree = defaultdict(int)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        
        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        taken_courses = 0
        
        
        while queue:
            current = queue.popleft()
            
            taken_courses += 1
            
            for nbr in graph[current]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return taken_courses == numCourses            
            
            
            
            
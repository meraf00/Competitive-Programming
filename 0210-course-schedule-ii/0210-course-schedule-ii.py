class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        
        queue = deque()
        
        for course, prereqs in enumerate(indegree):
            if prereqs == 0:
                queue.append(course)
        
        
        order = []
        
        while queue:
            node = queue.popleft()
            
            order.append(node)
            
            for nbr in graph[node]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        if len(order) == numCourses:
            return order
        
        return []
        
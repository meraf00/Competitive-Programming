"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)
        importance = defaultdict(int)
        
        for employee in employees:
            graph[employee.id] = employee.subordinates
            importance[employee.id] = employee.importance
        
        stack = [id]
        visited = set()                
        
        while stack:
            employee_id = stack.pop()                        
                        
            visited.add(employee_id)
            
            for neighbour in graph[employee_id]:
                if neighbour not in visited:
                    stack.append(neighbour)
        
        total_importance = 0
        for emp_id in visited:
            total_importance += importance[emp_id]
        
        
        return total_importance
            
            
            
        
        
        
        
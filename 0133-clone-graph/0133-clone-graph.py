"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        Node.__str__ = lambda obj : str(obj.val)
        Node.__repr__ = lambda obj : str(obj.val)   
        if not node:
            return None
                                
        visited = set([node.val])

        queue = deque([node])
        
        graph = {}

        while queue:
            current = queue.popleft()   
            
            if current.val not in graph:
                graph[current.val] = Node(current.val, set())                

            for node in current.neighbors:
                if node.val not in visited:                    
                    visited.add(node.val)
                    queue.append(node)
                    
                if node.val not in graph:
                    graph[node.val] = Node(node.val, set())

                graph[node.val].neighbors.add(graph[current.val])
                graph[current.val].neighbors.add(graph[node.val])
            
        return graph[1]

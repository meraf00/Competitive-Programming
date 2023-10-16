"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        levels = {}
        
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            
            if level in levels:
                levels[level].next = node
            
            levels[level] = node
            
            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        return root
        
        
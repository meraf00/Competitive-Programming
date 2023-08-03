"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_to_new_map = {None: None}
        
        current = head
        
        while current:
            if current not in old_to_new_map:
                old_to_new_map[current] = Node(current.val)
            
            if current.next and current.next not in old_to_new_map:
                old_to_new_map[current.next] = Node(current.next.val)
            
            if current.random and current.random not in old_to_new_map:
                old_to_new_map[current.random] = Node(current.random.val)
            
            old_to_new_map[current].next = old_to_new_map[current.next]
            old_to_new_map[current].random = old_to_new_map[current.random]
            
            current = current.next
        
        return old_to_new_map[head]
            
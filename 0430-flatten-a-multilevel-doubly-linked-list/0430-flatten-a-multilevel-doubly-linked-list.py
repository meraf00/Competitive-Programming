"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        if not head:
            return
        
        def flat(head):
            current = head
            prev = None
            
            while current:
                if current.child:
                    child_head, child_tail = flat(current.child)                    
                    
                    temp = current.next
                    
                    if child_head:
                        child_head.prev = current
                    
                    current.next = child_head
                    
                    if child_tail:
                        child_tail.next = temp
                    
                    if temp:
                        temp.prev = child_tail
                    
                    current = temp
                    prev = child_tail
                    
                    continue            
                
                prev = current
                current = current.next
        
            return head, prev
        
        head, tail = flat(head)
        
        current = head
        while current:
            current.child = None
            current = current.next
        
        
        head.prev = None
        tail.next = None
        
        return head
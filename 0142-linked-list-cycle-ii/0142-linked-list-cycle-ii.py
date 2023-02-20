# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle_(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
        
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        
        curr = head
        while curr:
            if curr in nodes:
                return curr
            
            nodes.add(curr)
            curr = curr.next
        
        return None
        
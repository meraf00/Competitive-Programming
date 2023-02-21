# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:                        
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head                
                while slow != fast:                    
                    fast = fast.next
                    slow = slow.next
                return slow
        
        return None
        
   
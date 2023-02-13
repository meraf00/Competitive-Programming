# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:        
        lh = less = ListNode()
        
        gh = greater = ListNode()
                
        current = head
        
        while current:
            
            if current.val < x:                                
                less.next = ListNode(current.val)  
                less = less.next
            else:
                greater.next = ListNode(current.val)  
                greater = greater.next
                
            current = current.next
        
        less.next = gh.next

        return lh.next
            

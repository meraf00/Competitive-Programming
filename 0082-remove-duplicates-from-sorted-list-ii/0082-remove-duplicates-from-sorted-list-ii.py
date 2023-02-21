# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        prev = dummy
        curr  = head
        
        last_seen = prev.val
        while curr:
            if curr.val == last_seen or (curr.next and curr.val == curr.next.val):
                if curr.next and curr.val == curr.next.val:
                    last_seen = curr.val                                        
                prev.next = curr.next
            else:
                last_seen = curr.val  
                prev =  curr
            
            curr = curr.next
        
        
        return dummy.next
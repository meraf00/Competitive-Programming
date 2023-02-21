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
        
        while curr:
            while prev.val == curr.val:
                curr = curr.next
                if not curr:
                    prev.next = curr
                    return dummy.next
            
            prev.next = curr
            prev = curr                        
            curr = curr.next
        
        return dummy.next
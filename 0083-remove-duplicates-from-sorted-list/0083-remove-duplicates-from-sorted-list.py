# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            while prev and curr and curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            
            if not curr:
                break
            prev = curr            
            curr = curr.next
            
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        tail = head
        prev = None
        curr = head        
        while curr:            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        return (prev, tail)
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        before_start = None
        start = None
        end = None
        prev = dummy
        
        curr = head
        index = 1
        while curr:            
            if index == left:
                before_start = prev
                start = curr
                
            if index == right:                
                end = curr                
                after_end = end.next
                end.next = None
                
                rev_start, rev_end = self.reverse(start)
                
                before_start.next = rev_start
                rev_end.next = after_end
                break
            
            index += 1
            prev = curr
            curr = curr.next
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def findMidAndPrev(self, head):
        fast = head
        slow = head
        prev  = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        
        return prev, slow
    
    def reverse(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
            
    def pairSum(self, head: Optional[ListNode]) -> int:
        preMid, midNode = self.findMidAndPrev(head)
        preMid.next = None  # split the node in half
        
        # reverse second half
        midNode = self.reverse(midNode)
        
        # find max twin sum
        max_sum = float('-inf')
        while midNode and head:
            current_sum = midNode.val + head.val
            max_sum = max(max_sum, current_sum)
            midNode = midNode.next
            head = head.next
        
        return max_sum
        
        
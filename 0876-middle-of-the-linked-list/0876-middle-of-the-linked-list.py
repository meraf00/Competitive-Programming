# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def middleNode__(self, head):
        array = []
        while head:
            array.append(head)
            head = head.next
        return array[len(array)//2]
            
        
    def middleNode_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:            
            length += 1
            curr = curr.next
        
        mid = length // 2
        curr = head
        while mid:
            mid -= 1
            curr = curr.next
        
        return curr
    
            
        
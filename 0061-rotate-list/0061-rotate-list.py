# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Use two pointers
        # Move front_pointer k steps ahead of back_pointer
        # Start moving both pointers until front_pointer runs out of the list
        # Split the linked list at back_pointer and insert the tails (2nd part of split)
        # at the front
                        
        length = self.getLength(head) 
        
        if not head or k % length == 0:
            return head
        
        k = k % length
                
        front_pointer = head        
        for _ in range(k):
            front_pointer = front_pointer.next
        
        back_pointer = head
        while front_pointer and front_pointer.next:
            back_pointer = back_pointer.next
            front_pointer = front_pointer.next                
                
        # find tail
        tail = back_pointer.next
        while tail and tail.next:
            tail = tail.next
                
        # insert in front
        tail.next = head
        
        # split the list
        new_head = back_pointer.next        
        back_pointer.next = None                        
        
        return new_head
        
        
        
        
            
        
        
            
        
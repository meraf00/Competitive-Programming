# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def kth_node(self, head, k):        
        current = head
        count  = 1
        while current and count < k:            
            count += 1
            current = current.next
        
        return current
    
    def reverse(self, head):
        current = head
        
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp                
        
        return prev
        
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        kth_node = self.kth_node(head, k)

        reverse = self.reverse(head)
        
        kth_from_back = self.kth_node(reverse, k)
        
        head = self.reverse(reverse)
        
        after_kth_node = kth_node.next
        after_kth_from_back = kth_from_back.next
        
        dummy = ListNode(next=head)
        
        current = dummy  
        
        while current:            
            if current.next == kth_node:                
                current.next = kth_from_back
                kth_from_back.next = after_kth_node
            
            elif current.next == kth_from_back:
                current.next = kth_node
                kth_node.next = after_kth_from_back
            
            current = current.next
                
        return dummy.next
        
        
        
        
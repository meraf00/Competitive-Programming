# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, head, node):
        dummy = ListNode(float("-inf"))
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            if node.val <= curr.val:
                prev.next = node
                node.next = curr
                return dummy.next
            prev = curr
            curr = curr.next
        
        prev.next = node
        node.next = None
        
        return dummy.next
            
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr:
            if curr.next and curr.val > curr.next.val:
                node = curr.next
                curr.next = curr.next.next
                head = self.insert(head, node)
                continue
                        
            curr = curr.next
                
        return head
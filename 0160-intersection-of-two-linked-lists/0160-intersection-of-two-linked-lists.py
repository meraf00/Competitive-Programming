# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        
        current_a = headA
        current_b = headB
        
        while current_a or current_b:
            if current_a in seen:
                return current_a
            
            if current_b in seen:
                return current_b
            
            if current_a == current_b:
                return current_b
            
            if current_a:            
                seen.add(current_a)
                current_a = current_a.next
            
            if current_b:
                seen.add(current_b)
                current_b = current_b.next
        
        
        
        
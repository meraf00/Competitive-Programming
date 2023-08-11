# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        current = head
        
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
                        
            stack.append(current)
            
            current = current.next
        
        for idx in range(len(stack) - 1):
            stack[idx].next = stack[idx + 1]
        
        stack[-1].next = None        
        
        return stack[0]
                
            
            
            
            
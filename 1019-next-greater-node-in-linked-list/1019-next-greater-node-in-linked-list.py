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
    
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        
        length = self.getLength(head)
        answer = [0] * length
        
        current_index = 0
        current = head
        while current:            
            while stack and stack[-1][0] < current.val:
                _, index = stack.pop()
                answer[index] = current.val
            
            stack.append((current.val, current_index))
            current_index += 1
            current = current.next
                
            
        return answer
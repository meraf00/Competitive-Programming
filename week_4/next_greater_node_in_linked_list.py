"""
https://leetcode.com/problems/next-greater-node-in-linked-list/
"""


from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:        
        
        stack = []
        current = head
        while current:
            while len(stack) and stack[-1].val < current.val:
                stack.pop().nextLarger = current
            
            stack.append(current)
            current = current.next
                
        output = []
        while head:
            if hasattr(head, 'nextLarger'):
                output.append(head.nextLarger.val)
            else:
                output.append(0)
            head = head.next
        
        return output
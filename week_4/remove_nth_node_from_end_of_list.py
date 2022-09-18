"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        current = head
        while current:
            length += 1
            current = current.next
        
        i = length - n
        current = head
        prev = None
        while current and i > 0:            
            prev = current
            current = current.next
            i -= 1
        
        if prev:
            prev.next = current.next if current and current.next else None        
        else: # remove head
            head = head.next
        
        return head
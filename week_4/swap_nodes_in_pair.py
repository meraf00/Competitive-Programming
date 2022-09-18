"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        if head and head.next:
            head = head.next
        
        prev = None
        while current and current.next:
            nxt = current.next.next
            current.next.next = current            
            if prev:
                prev.next = current.next
            prev = current
            current.next = None
            current = nxt
        
        if current and prev:
            prev.next = current
            current.next = None
        return head
        
"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        copy = []
        while head:
            copy.append(head.val)
            head = head.next
                
        for i in range(0, len(copy), k):
            if i + k - 1 < len(copy):
                for j, val in enumerate(reversed(copy[i: i+k])):
                    copy[i+j] = val
        
        head = None
        current = None
        for val in copy:
            if not head:
                head = ListNode(val)
                current = head
                continue
            current.next = ListNode(val)
            current = current.next
        return head
from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next:Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        right = self.middleNode(head)
        reversed_right = self.reverseLinkedList(right)

        while reversed_right:
            if left.val != reversed_right.val:
                return False
            left = left.next
            reversed_right = reversed_right.next
        return True

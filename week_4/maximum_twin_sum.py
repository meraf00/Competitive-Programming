"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.findMid(head)
        reversed_2nd_half = self.reverse(mid)
        
        max_sum = 0
        while reversed_2nd_half:
            max_sum = max(max_sum, reversed_2nd_half.val + head.val)
            head = head.next
            reversed_2nd_half = reversed_2nd_half.next
        
        return max_sum
    
    # easy soln
    def pairSum_(self, head: Optional[ListNode]) -> int:
        copy = []
        
        while head:
            copy.append(head.val)
            head = head.next
    
        max_sum = 0
        for i in range(len(copy) // 2 + 1):
            max_sum = max(max_sum, copy[i] + copy[len(copy)-1-i])
            
        return max_sum
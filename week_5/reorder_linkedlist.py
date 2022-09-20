"""
https://leetcode.com/problems/reorder-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        mid_reversed = self.reverse(slow)
        
        if not prev:            
            return
        
        prev.next = None
        
        reordered = head          
        while head and mid_reversed:             
            temp1 = head.next
            temp2 = mid_reversed.next
            
            head.next = mid_reversed
            if temp1:
                mid_reversed.next = temp1
                                                
            head = temp1
            mid_reversed = temp2
"""
https://leetcode.com/problems/sort-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
                
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
        
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        
        while l2:                   
            current.next = l2
            l2 = l2.next
            current = current.next        
        return head
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next            
            
        if prev:
            prev.next = None                          
            return self.merge(self.sortList(head), self.sortList(slow))
        return head
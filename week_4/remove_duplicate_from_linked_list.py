"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:             
        new = None
        current = head
        prev = None
        repeated = None
        while current:                 
            if current.next and current.next.val == current.val:
                repeated = current.val
                
                while current and current.val == repeated:
                    current = current.next                
            else:                
                if not prev:
                    prev = current
                    new = prev
                else:
                    prev.next = current
                    prev = current                
                current = current.next
        
        if prev:
            prev.next = None        
            
        return new
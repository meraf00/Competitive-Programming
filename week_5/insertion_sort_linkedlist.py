"""
https://leetcode.com/problems/insertion-sort-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        current_prev = head
        while current:            
            node = head 
            prev = None
            while node and current.val > node.val:                
                prev = node
                node = node.next 
            
            if node == current:
                current_prev = current
                current = current.next
                continue
            
            temp = current.next
            if prev == None:                
                current.next = head
                head = current                                               
            else:
                prev.next = current  
                current.next = node                
                
            current_prev.next = temp 
            current = temp                
            
        return head
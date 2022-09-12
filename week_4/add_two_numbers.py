"""
https://leetcode.com/problems/add-two-numbers/submissions/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:           
        carry = 0
        result = None  
        current = None
        
        while l1 and l2:
            partial_addition = l1.val + l2.val + carry
            carry = partial_addition // 10             
            
            if result == None:
                result = ListNode()
                current = result
            else:
                current.next = ListNode()
                current = current.next
                
            current.val += partial_addition % 10                                                
            
            l1 = l1.next
            l2 = l2.next
                
        while l1:
            current.next = ListNode()
            current = current.next
            
            partial_addition = l1.val + carry
            carry = partial_addition // 10 
            
            current.val += partial_addition % 10 
            
            l1 = l1.next                        
        
        while l2:
            current.next = ListNode()
            current = current.next
            
            partial_addition = l2.val + carry
            carry = partial_addition // 10 
            
            current.val += partial_addition % 10 
            l2 = l2.next                                        
        
        while carry:
            current.next = ListNode(carry)
            current = current.next
            carry = carry // 10 
            
        return result
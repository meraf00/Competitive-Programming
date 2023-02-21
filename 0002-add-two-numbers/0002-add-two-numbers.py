# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        current = head
        carry =  0
        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            
            if digit_sum > 9:
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            else:
                carry = 0
                
            current.next = ListNode(digit_sum)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            digit_sum = l1.val + carry
            
            if digit_sum > 9:                
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            else:
                carry = 0
            
            current.next = ListNode(digit_sum) 
            current = current.next
            l1 = l1.next
        
        while l2:
            digit_sum = l2.val + carry
            
            if digit_sum > 9:
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            else:
                carry = 0
            current.next = ListNode(digit_sum)
            current = current.next
            l2 = l2.next
        
        if carry:
            current.next = ListNode(carry)
            current = current.next
            
        return head.next
            
                
                
                
            
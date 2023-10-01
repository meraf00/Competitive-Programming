# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        current = l1
        while current:
            num1.append(current)
            current = current.next
        
        current = l2
        while current:
            num2.append(current)
            current = current.next
        
        ans = None
        carry = 0
        
        while num1 and num2:
            digit_sum = num1.pop().val + num2.pop().val + carry
            
            if digit_sum < 10:
                ans = ListNode(digit_sum, ans)
                carry = 0
            
            else:
                ans = ListNode(digit_sum % 10, ans)
                carry = 1
        
        for arr in [num1, num2]:
            while arr:
                digit_sum = carry + arr.pop().val

                if digit_sum < 10:
                    ans = ListNode(digit_sum, ans)
                    carry = 0

                else:
                    ans = ListNode(digit_sum % 10, ans)
                    carry = 1
        
        if carry == 1:
            ans = ListNode(1, ans)
            
        return ans
        
        
            
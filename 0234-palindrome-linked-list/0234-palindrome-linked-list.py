# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        fast = head
        slow = head
             
        prev = None
        while fast and fast.next:
            fast = fast.next.next            
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None            
        return slow
    
    def reverse(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev            
            prev = current     
            current = temp
        
        return prev
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)
        
        mid = self.reverse(mid)
        
        while head and mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        
        return True
            
            
        
        
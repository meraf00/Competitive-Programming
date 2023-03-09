# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        dummy = ListNode()
        
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
            
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2
        
        return dummy.next
            
                        
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
    

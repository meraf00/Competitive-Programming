# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, l1, l2):
        dummy = ListNode() 
        
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next    
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        merged = lists[0]
        for lst in lists[1:]:
            merged = self.merge2Lists(merged, lst) 
            
        return merged
            
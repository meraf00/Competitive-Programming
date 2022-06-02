from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        head = None
        tail = None
        current = None
        while list1 and list2:
            if list1.val <= list2.val:
                current = list1
                list1 = list1.next
            else:
                current = list2
                list2 = list2.next
            
            if not head:
                head = current
                tail = current
            else:
                tail.next = current
                tail = current 

        if list1:
            if tail:
                tail.next = list1
            else:
                head = list1
        if list2:
            if tail:
                tail.next = list2         
            else:
                head = list2
               
        return head






if __name__ == "__main__":
    l = ListNode()
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)

    l2 = ListNode()
    l2.next = ListNode(5)
    l2.next.next = ListNode(6)
    l2.next.next.next = ListNode(6)

    
    s = Solution()
    merged = s.mergeTwoLists(l, l2)

    while merged:
        print(merged.val)
        merged = merged.next


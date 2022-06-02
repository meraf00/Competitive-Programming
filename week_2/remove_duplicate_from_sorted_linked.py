from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
            else:            
                current = current.next
        return head

        






if __name__ == "__main__":
    l2 = ListNode()
    l2.next = ListNode(5)
    l2.next.next = ListNode(6)
    l2.next.next.next = ListNode(6)

    
    s = Solution()
    cleand = s.deleteDuplicates(l2)

    while cleand:
        print(cleand.val)
        cleand = cleand.next


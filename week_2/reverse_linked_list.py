from tkinter import N
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:           
        stack = []
        
        while head:
            stack.append(head)
            head = head.next
        
        if len(stack):
            head = stack.pop()
            current = head
            while len(stack):
                current.next = stack.pop()
                current = current.next

            current.next = None
        return head

if __name__ == "__main__":
    l = ListNode()
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)

    c = l    
    while c:
        print(c.val)
        c = c.next
    print("------------")
    r = Solution()
    re = r.reverseList(l)

    c = re   
    while c:
        print(c.val)
        c = c.next

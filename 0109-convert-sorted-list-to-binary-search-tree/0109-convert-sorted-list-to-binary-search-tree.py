# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        
        def build_bst(values, left, right):
            if right < left:
                return
            
            if left == right:
                return TreeNode(values[left])
            
            mid = (left + right) // 2
            
            node = TreeNode(values[mid])
            
            node.left = build_bst(values, left, mid - 1)
            node.right = build_bst(values, mid + 1, right)
            
            return node
        
        return build_bst(values, 0, len(values) - 1)
            
            
            
        
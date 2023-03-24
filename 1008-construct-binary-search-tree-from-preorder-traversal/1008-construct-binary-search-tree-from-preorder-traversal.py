# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, num):
        if not root:
            return TreeNode(num)
        
        if root.val > num:
            root.left = self.insert(root.left, num)
        
        elif root.val < num:
            root.right = self.insert(root.right, num)
        
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        
        for num in preorder:
            root = self.insert(root, num)
        
        return root
            
            
            
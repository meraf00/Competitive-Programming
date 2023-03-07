# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, root):
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.swap(root.left)
        self.swap(root.right)
        
        return root
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or not p and q:
            return False
        
        elif not p and not q:
            return True
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        right_fliped = self.swap(root.right)
        
        return self.isSameTree(right_fliped, root.left)
        
        
        
        
        
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        @cache
        def isEquiv(r1, r2):
            if not r1 and not r2:
                return True
            
            if r1 and not r2:
                return False
            
            if r2 and not r1:
                return False
            
            if r1.val == r2.val:
                return (isEquiv(r1.left, r2.left) and isEquiv(r1.right, r2.right)) or (isEquiv(r1.left, r2.right) and isEquiv(r1.right, r2.left))
            
            
            return False
        
        return isEquiv(root1, root2)
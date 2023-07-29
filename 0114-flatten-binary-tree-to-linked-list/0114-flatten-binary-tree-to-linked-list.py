# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        if not root:
            return
        
        if not root.left and not root.right:
            return root
        
        
        left = root.left
        right = root.right                                       
                
        if left:
            root.left = None
            root.right = left 
            left_leaf = self.flatten(left)
            left_leaf.right = right
        
        if right:
            right_leaf = self.flatten(right)                            
            return right_leaf
        
        return left_leaf
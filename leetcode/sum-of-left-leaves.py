# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_of_left_leaves(root, isLeft):
            if not root:
                return 0
            
            if isLeft and not root.left and not root.right:                
                return root.val
            
            sum_left = sum_of_left_leaves(root.left, True)
            sum_right = sum_of_left_leaves(root.right, False)
            
            return sum_left + sum_right
        
        return sum_of_left_leaves(root, False)
            
            
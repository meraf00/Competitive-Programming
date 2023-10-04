# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(root):
            if not root:
                return (0, 0)
            
            left_broken, left_unbroken = dp(root.left)
            right_broken, right_unbroken = dp(root.right)
            
            # self unbroken
            unbroken = max(left_broken, left_unbroken) + max(right_broken, right_unbroken)
            
            # self broken
            broken = left_unbroken + right_unbroken + root.val
            
            return (broken, unbroken)
    
        broken, unbroken = dp(root)
        
        return max(broken, unbroken)
            
            
        
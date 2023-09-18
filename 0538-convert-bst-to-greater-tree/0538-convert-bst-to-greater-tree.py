# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def gst(root, parent_right_sum):    
            if not root:
                return 0
            
            val = root.val
            
            right_sum = gst(root.right, parent_right_sum)
            
            root.val += right_sum + parent_right_sum
            
            left_sum = gst(root.left, root.val)
            
            return val + right_sum + left_sum
            
        
        gst(root, 0)
        
        return root
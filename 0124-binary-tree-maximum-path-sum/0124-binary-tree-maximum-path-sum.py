# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')
        
        has_non_negative = False
        
        max_negative = float('-inf')
        
        def max_sum(node):   
            nonlocal maximum, has_non_negative, max_negative
            
            if node.val >= 0:
                has_non_negative = True
                
            if node.val < 0:
                max_negative = max(max_negative, node.val)
            
            if not node.left and not node.right:
                maximum = max(maximum, node.val)
                return node.val
              
            max_child = 0
            
            include_node = node.val
            
            if node.left:
                left_sum = max_sum(node.left)
                max_child = max(left_sum, max_child)
                include_node += left_sum
            
            if node.right:
                right_sum = max_sum(node.right)
                max_child = max(right_sum, max_child)                        
                include_node += right_sum
            
            maximum = max(maximum, include_node, max_child, max_child + node.val, node.val)
            
            return node.val + max_child
        
        max_sum(root)
        
        if not has_non_negative:
            maximum = max_negative
        
        return maximum
            
            
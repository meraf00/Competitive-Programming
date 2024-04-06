# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def average_of_subtree(node):
            if not node:
                return 0, 0, 0
            
            left_count, left_sum, lc = average_of_subtree(node.left)
            right_count, right_sum, rc = average_of_subtree(node.right)
            
            subtree_count = 1 + left_count + right_count
            subtree_sum = node.val + left_sum + right_sum
            
            count = lc + rc
            
            if node.val == subtree_sum // subtree_count:
                count += 1
            
            return subtree_count, subtree_sum, count
    
        return average_of_subtree(root)[-1]
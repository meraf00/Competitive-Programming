# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        
        def find_max_sum(node):
            nonlocal max_sum
            
            if not node:                
                return 0, inf, -inf
            
            lsum, lmin, lmax = find_max_sum(node.left)
            rsum, rmin, rmax = find_max_sum(node.right)
            
            if lmax < node.val < rmin:     
                sum_ = node.val + lsum + rsum
                max_sum = max(max_sum, sum_)
                return sum_, min(lmin, node.val), max(rmax, node.val)
            
            else:
                return 0, -inf, inf
        
        find_max_sum(root)
        
        return max_sum
                
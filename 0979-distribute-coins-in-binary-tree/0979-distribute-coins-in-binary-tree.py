# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        count = 0
        
        def distribute(node):
            nonlocal count
            
            if not node:
                return 0
            
            # node.val = surplus 
            # (if node.val is + -> surplus, - -> deficit, 0 -> has 1 coin)
            node.val = node.val - 1
            
            surplus_left = distribute(node.left)
            
            surplus_right = distribute(node.right)
            
            # amount of coins moving up or down the tree
            count += abs(surplus_left) + abs(surplus_right)            
                                
            return node.val + surplus_left + surplus_right
        
        distribute(root)
        
        return count
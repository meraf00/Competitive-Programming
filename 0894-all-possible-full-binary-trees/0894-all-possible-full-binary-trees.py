# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:        
        if n % 2 == 0:
            return []
        
        dp = [[] for _ in range(n + 1)]        
        dp[1].append(TreeNode())
        
        for n_nodes in range(3, n + 1, 2):
            for i in range(1, n_nodes - 1, 2):
                j = n_nodes - i - 1
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[n_nodes].append(root)
        
        return dp[n]
        
        
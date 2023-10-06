# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        
        def dfs(root, path, path_sum):                            
            if root and not root.left and not root.right:
                if path_sum == targetSum:                    
                    paths.append(path[:])                    
                
                return
                        
            if root.left:
                path.append(root.left.val)
                dfs(root.left, path, path_sum + root.left.val)
                path.pop()
            
            if root.right:
                path.append(root.right.val)
                dfs(root.right, path, path_sum + root.right.val)
                path.pop()
        
        if root:
            dfs(root, [root.val], root.val)
        
        return paths
                
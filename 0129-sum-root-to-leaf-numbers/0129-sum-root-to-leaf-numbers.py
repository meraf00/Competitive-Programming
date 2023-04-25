# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        current = [str(root.val)]
        
        def dfs(node):
            
            nonlocal current
            
            if not node.left and not node.right:
                nums.append("".join(current))
                return        
                        
            if node.left:
                current.append(str(node.left.val))
                dfs(node.left)
                current.pop()
            
            if node.right:
                current.append(str(node.right.val))
                dfs(node.right)
                current.pop()
            
        
        dfs(root)
        
        return sum(map(int, nums))
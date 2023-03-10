# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []
        
        current_path = [str(root.val)]
        
        def backtrack(root):
            if not root:
                return
            
            if not root.left and not root.right:
                paths.append("->".join(current_path))
                return
            
                                    
            if root.left:
                current_path.append(str(root.left.val))
                backtrack(root.left)
                current_path.pop()

            
            if root.right:
                current_path.append(str(root.right.val))
                backtrack(root.right)
                current_path.pop()            
        
        backtrack(root)
        
        return paths
            
        
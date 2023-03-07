# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        
        current = root
        
        last_seen = float('-inf')
        
        while True:
            if current:
                stack.append(current)
                current = current.left
                
                
            elif stack:
                current = stack.pop()
                
                if last_seen < current.val:
                    last_seen = current.val
                else:
                    return False
                
                current = current.right
                
                
            else:
                break
        
        return True
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        current = root
        
        node_count = 0
        
        while True:
            if current != None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                node_count += 1
                current = current.right
            
            else:
                break
        
        return node_count
                
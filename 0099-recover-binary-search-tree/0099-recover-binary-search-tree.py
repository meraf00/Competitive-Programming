# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """  
        
        node1 = None
        node2 = None
                
        def recover(node, prev):
            nonlocal node1, node2
            
            if not node:
                return prev
            
            left = recover(node.left, prev)                        
            
            if left and left.val > node.val:                
                if not node1:
                    node1 = left
                    node2 = node
                else:
                    node2 = node
            
            right = recover(node.right, node)
            
            return right
            
        recover(root, None)                
        
        node1.val, node2.val = node2.val, node1.val
       




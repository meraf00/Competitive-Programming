# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        current = root
        
        common_parent = None
        
        while current:
            
            if p.val == current.val:
                break
            
            elif current.val < p.val:
                current = current.right
            
            elif current.val > p.val:                
                
                if current.val <= q.val:
                    if not common_parent:
                        common_parent = current                    
                
                current = current.left 
        
        if common_parent:            
            return common_parent
        
        current = root
        
        while current:
            
            if q.val == current.val:
                break
            
            elif current.val < q.val:
                if current.val >= p.val:
                    if not common_parent:
                        common_parent = current
                    
                current = current.right
           
            elif current.val > q.val:
                current = current.left 
                
        return common_parent
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':                
        
        def dfs(root): 
            has_p = has_q = False
            
            if not root:
                return None, has_p, has_q
            
            if root == p:
                has_p = True
            
            if root == q:
                has_q = True
            
            
            if has_p and has_q:                
                return root, has_p, has_q                        
            
            cpl, hpl, hql = dfs(root.left)
            cpr, hpr, hqr = dfs(root.right)
            
            if hpl and hql:                
                return cpl, hpl, hql
            
            if hpr and hqr:            
                return cpr, hpr, hqr
            
            return root, hpl or hpr or has_p, hql or hqr or has_q

        cp, _, _ = dfs(root)
        
        
        return cp
            
            
            
            
            
            
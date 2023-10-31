# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        to_delete = set(to_delete)
        
        new_roots = set([root])
        
        def del_nodes(root, parent_left, parent_right):
            if not root:
                return
            
            if root.val in to_delete:
                if root.left:
                    new_roots.add(root.left)
                
                if root.right:
                    new_roots.add(root.right)
                
                if parent_right:
                    parent_right.right = None
                
                if parent_left:
                    parent_left.left = None
            
                if root in new_roots:
                    new_roots.remove(root)
            
            del_nodes(root.left, root, None)
            del_nodes(root.right, None, root)
    
        del_nodes(root, None, None)
                  
        return new_roots
            
            
                
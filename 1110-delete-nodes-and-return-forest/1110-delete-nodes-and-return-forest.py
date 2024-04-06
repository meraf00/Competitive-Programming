# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        
        forest = []
        
        if root and root.val not in to_delete:
            forest.append(root)
        
        def delete_nodes(node):
            if not node:
                return
            
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    forest.append(node.left)
                
                if node.right and node.right.val not in to_delete:
                    forest.append(node.right)
                    
                delete_nodes(node.left)
                delete_nodes(node.right)
                return None                        
            
            node.left = delete_nodes(node.left)
            node.right = delete_nodes(node.right)                        
                        
            return node
        
        delete_nodes(root)
    
        return forest
            
            
                
            
                
                
        
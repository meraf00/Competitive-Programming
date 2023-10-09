# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        found = []
        
        def build_hash(root):                        
            if not root:
                return (None, )
        
            left_hash = build_hash(root.left)
            right_hash = build_hash(root.right)                        
            
            root_hash = (root.val, *right_hash, *left_hash)
            
            if seen[root_hash] == 1:
                found.append(root)
            
            seen[root_hash] += 1
            
            return root_hash
    
        build_hash(root)
        
        return found
    

                
            
            
            
            
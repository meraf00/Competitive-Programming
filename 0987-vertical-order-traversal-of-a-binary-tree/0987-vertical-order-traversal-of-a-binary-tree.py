# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        traversal = defaultdict(list)
                        
        
        stack = [(root, 0, 0)]
        
        min_col = float('inf')
        max_col = float('-inf')
        
        while stack:
            node, row, col = stack.pop()
            
            traversal[col].append((row, node.val))
            
            if node.right:
                stack.append((node.right, row + 1, col + 1))
            
            if node.left:
                stack.append((node.left, row + 1, col - 1))
            
            max_col = max(col, max_col)
            min_col = min(col, min_col)
                        
        
        output = []
        for i in range(min_col, max_col + 1):
            traversal[i].sort()            
            output.append(list(map(lambda x: x[1],  traversal[i])))
                        
        return output
                
    
    
    
    
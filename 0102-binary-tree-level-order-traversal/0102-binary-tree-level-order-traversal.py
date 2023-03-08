# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        queue = deque()
                        
        queue.append((root, 0))
        
        levels = defaultdict(list)
        
        max_level = 0
        
        while queue:
            current, level = queue.popleft()
            
            max_level = max(level, max_level)
            
            levels[level].append(current.val)
            
            if current.left:                
                queue.append((current.left, level + 1))
            
            if current.right:
                queue.append((current.right, level + 1))
        
        output = [None] * (max_level + 1)
        
        for level, nodes_val in levels.items():
            output[level] = nodes_val
        
        return output
        
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        
        max_level = 0
        level_sum = 0
        
        while queue:
            node, level = queue.popleft()
            
            if level == max_level:
                level_sum += node.val
            
            elif level > max_level:
                max_level = level
                level_sum = node.val
            
            
            if node.right:
                queue.append((node.right, level + 1))
            
            if node.left:
                queue.append((node.left, level + 1))
            
        
        return level_sum
            
    
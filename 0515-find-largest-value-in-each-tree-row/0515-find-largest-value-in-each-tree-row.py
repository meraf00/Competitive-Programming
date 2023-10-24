# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        
        max_value = defaultdict(lambda: float('-inf'))
        
        max_level = 0
        
        while queue:
            node, level = queue.popleft()
            
            max_value[level] = max(node.val, max_value[level])
            
            max_level = max(max_level, level)
            
            
            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        
        ans = []
        
        for i in range(max_level + 1):
            ans.append(max_value[i])
        
        return ans
            
        
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        queue = deque()
        
        queue.append((root, 0))
        
        right_most = defaultdict(TreeNode)
        
        max_level = 0
        
        while queue:
            current, level = queue.popleft()
            
            right_most[level] = current.val
            
            max_level = max(level, max_level)
            
            if current.left:
                queue.append((current.left, level + 1))
            
            if current.right:
                queue.append((current.right, level + 1))
        
        output = [0] * (max_level + 1)
        
        for i in range(max_level + 1):
            output[i] = right_most[i]
        
        return output
        
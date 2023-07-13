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
        
        level = defaultdict(lambda: float('-inf'))
        
        max_depth = 0
        
        while queue:
            current, depth = queue.popleft()
            
            level[depth] = max(level[depth], current.val)
            
            max_depth = max(depth, max_depth)
            
            
            if current.left:
                queue.append((current.left, depth + 1))
            
            if current.right:
                queue.append((current.right, depth + 1))
        
        answer = [0] * (max_depth + 1)
        
        for i in range(max_depth + 1):
            answer[i] = level[i]
        
        return answer
        
                
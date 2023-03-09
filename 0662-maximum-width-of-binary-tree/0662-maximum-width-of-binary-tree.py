# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # contains <level: [left most, right most]>
        traversed = defaultdict(lambda : [float('inf'), float('-inf')])
        
        queue = deque()                
        
        queue.append((root, 0, 1))                
        
        while queue:
            current, level, width = queue.popleft()
            
            if current.left:               
                queue.append((current.left, level + 1, width * 2 - 1))
            
            if current.right:
                queue.append((current.right, level + 1, width * 2))
            
            left_most, right_most = traversed[level]
            
            traversed[level][0] = min(left_most, width)
            traversed[level][1] = max(right_most, width)
            
        
        max_width = 0
        
        for left_most, right_most in traversed.values():
            max_width = max(max_width, right_most - left_most + 1)
        
        
        return max_width
        
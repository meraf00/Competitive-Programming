# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([(root, 0)])
        
        level_average = defaultdict(lambda : [0, 0])
        
        max_level = 0
        
        while queue:
            node, level = queue.popleft()
            
            max_level = max(max_level, level)
            
            level_average[level][0] += node.val
            level_average[level][1] += 1
            
            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        ans = [0] * (max_level + 1)
        
        for k, v in level_average.items():
            
            ans[k] = v[0] / v[1]
        
        return ans
        
        
            
            
            
        
        
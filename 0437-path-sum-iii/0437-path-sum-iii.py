# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        counter = defaultdict(int)
        counter[0] = 1   
        
        count = 0
        
        def dfs(root, running_sum):
            nonlocal count
            
            if not root:                
                return
            
            running_sum += root.val                        
                        
            count += counter[running_sum - targetSum]
            
            counter[running_sum] += 1
            
            dfs(root.left, running_sum)
            
            dfs(root.right, running_sum)
            
            counter[running_sum] -= 1
                        
        
        dfs(root, 0)
    
        return count
        
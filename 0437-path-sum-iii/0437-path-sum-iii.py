# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def count_path(self, node, counter, running_sum, target_sum):
        if not node:
            return
        
        running_sum += node.val                
        
        self.total_path += counter[running_sum - target_sum]
        
        counter[running_sum] += 1
        
        self.count_path(node.left, counter, running_sum, target_sum)                  
        
        self.count_path(node.right, counter, running_sum, target_sum)
        
        counter[running_sum] -= 1
        
                
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        running_sum = 0
        
        counter = defaultdict(int)
        
        counter[0] = 1
                                                       
        self.total_path = 0
        
        self.count_path(root, counter, running_sum, targetSum)
        
        return self.total_path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, start_index, end_index):
        if start_index > end_index:
            return None
        
        
        if start_index == end_index:
            return TreeNode(self.nums[start_index])                
                
          
        
        max_num = max(self.nums[start_index:end_index+1])
        
        index = self.num_index[max_num]
                
        left_subtree = self.buildTree(start_index, index - 1)
        
        right_subtree = self.buildTree(index + 1, end_index)
        
        
        
        root = TreeNode(max_num, left_subtree, right_subtree)
                
        return root
                        
        
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        self.num_index = {}      
        self.nums = nums

        
        for index, num in enumerate(nums):
            self.num_index[num] = index
            
        
        return self.buildTree(0, len(nums) - 1)
        
        
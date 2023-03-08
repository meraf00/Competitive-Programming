# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sum_count_ave_count(self, root):
        # returns (sum of all nodes in the sub tree,
        #          number of nodes, 
        #          num of all nodes that are equal to average of sub tree)
        
        if not root:
            return (0, 0, 0)
        
        if not root.left and not root.right:
            return (root.val, 1, 1)
        
        
        left_sum, left_count, left_averages = self.sum_count_ave_count(root.left)
        
        right_sum, right_count, right_averages = self.sum_count_ave_count(root.right)
        
        
        num_of_nodes_in_sub_tree = left_count + right_count + 1
        
        sum_of_vals_in_sub_tree = left_sum + right_sum + root.val
        
        ave = sum_of_vals_in_sub_tree // num_of_nodes_in_sub_tree
        
        
        if ave == root.val:
            total_averages = left_averages + right_averages + 1
        
        else:
            total_averages = left_averages + right_averages
            
        return (sum_of_vals_in_sub_tree, num_of_nodes_in_sub_tree, total_averages)
                        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _, _, total_averages = self.sum_count_ave_count(root)
        
        return total_averages
        
        
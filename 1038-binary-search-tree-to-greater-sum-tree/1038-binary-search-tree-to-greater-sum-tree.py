# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def gst(root, key_sum):    
            if not root: 
                return key_sum
                      
            right_sum = gst(root.right, key_sum)            
            
            node_key =  right_sum + root.val
            
            root.val = node_key
            
            left_sum = 0
            
            if root.left:
                left_sum = gst(root.left, node_key)
            
            return max(node_key, left_sum)
        
        gst(root, 0)
        
        return root
                
            
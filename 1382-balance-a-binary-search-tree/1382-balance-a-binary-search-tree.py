# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_list(self, root):
        nodes = []
        
        stack = []        
        
        while True:
            if root:
                stack.append(root)
                root = root.left
                        
            elif stack:
                root = stack.pop()
                nodes.append(root)
                root = root.right
                        
            else:
                break
        
        
        return nodes
            
    
    def build_balanced_tree(self, nodes, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        
        root = nodes[mid]
        
        root.left = self.build_balanced_tree(nodes, start, mid - 1)
        root.right = self.build_balanced_tree(nodes, mid + 1, end)
        
        return root
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes_sorted = self.build_list(root)
        
        return self.build_balanced_tree(nodes_sorted, 0, len(nodes_sorted) - 1)
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, depth=0):
            if not node:
                return depth
            
            max_depth = depth + 1
            
            for child in node.children:
                max_depth = max(dfs(child, depth + 1), max_depth)
            
            return max_depth
        
        return dfs(root)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, target_depth: int) -> Optional[TreeNode]:       
        if target_depth == 1:
            return TreeNode(val, left=root)
        
        queue = deque([(root, 1)])
        
        visited = set([root])
        
        nodes = []
                
                
        while queue:
            current, depth = queue.popleft()
                        
            if depth == target_depth - 1:
                nodes.append(current)
                
            if current.left:
                queue.append((current.left, depth + 1))
                visited.add(current.left)
            
            if current.right:
                queue.append((current.right, depth + 1))
                visited.add(current.right)
        
        
        for node in nodes:
            prev_left = node.left
            prev_right = node.right
            
            node.left = TreeNode(val, left=prev_left)
            node.right = TreeNode(val, right=prev_right)
            
        return root
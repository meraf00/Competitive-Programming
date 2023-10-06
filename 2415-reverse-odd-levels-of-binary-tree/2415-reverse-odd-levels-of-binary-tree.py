# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])
        
        while queue:            
            current, level = queue.popleft()    
            
            in_level = []
            
            if level & 1:  
                queue.appendleft((current, level))
                
                while queue:                                        
                    node, lvl = queue[0]

                    if lvl != level:
                        break

                    node, lvl = queue.popleft()                                

                    in_level.append(node)
                    

                    if node.left:
                        queue.append((node.left, lvl + 1))

                    if node.right:
                        queue.append((node.right, lvl + 1))
                
            else:
                if current.left:
                    queue.append((current.left, level + 1))

                if current.right:
                    queue.append((current.right, level + 1))
            
            
            for i in range(len(in_level) // 2):
                in_level[i].val, in_level[~i].val = in_level[~i].val, in_level[i].val                        
                        
        return root
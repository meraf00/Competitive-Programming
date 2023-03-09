# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        
        stack = []
        
        current = root
        
        last_seen = float("-inf")
        max_count = float("-inf")
        
        count = 0
        
        while True:
            if current:
                stack.append(current)
                current = current.left
            
            
            elif stack:
                current = stack.pop()
                
                if last_seen != current.val:
                    if count == max_count:
                        modes.append(last_seen)
                    
                    elif count > max_count:
                        max_count = count
                        modes = [last_seen]
                                            
                    count = 0                                        
                    
                count += 1
                
                last_seen = current.val
                
                current = current.right
            
            else:
                if count == max_count:
                    modes.append(last_seen)
                    
                elif count > max_count:
                    max_count = count
                    modes = [last_seen]
                                                                
                break
        
        return modes
                
                
                    
                
                
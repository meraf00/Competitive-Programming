# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        
        ans = []
        
        while queue:
            number_of_elements = len(queue)
            total_sum = 0
            
            for _ in range(number_of_elements):            
                node = queue.popleft()
                
                total_sum += node.val                
            
            
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            ans.append(total_sum / number_of_elements)

        
        return ans
        
        
            
            
            
        
        
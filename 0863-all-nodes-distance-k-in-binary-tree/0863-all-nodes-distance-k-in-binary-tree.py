# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        stack = []
        current = root
        
        while True:
            
            if current:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                
                if current.left:
                    graph[current.val].append(current.left.val)
                    graph[current.left.val].append(current.val)
                
                if current.right:
                    graph[current.val].append(current.right.val)
                    graph[current.right.val].append(current.val)
                
                current = current.right
            
            else:
                break
        
        
        
        ans = []
        
        queue = deque([(target.val, 0)])
        
        visited = set([target.val])
                
        while queue:
            current, distance = queue.popleft()
            
            if distance == k:
                ans.append(current)
            
            for nbr in graph[current]:
                if nbr not in visited:
                    queue.append((nbr, distance + 1))
                    visited.add(nbr)
                
            
        return ans
            
            
        
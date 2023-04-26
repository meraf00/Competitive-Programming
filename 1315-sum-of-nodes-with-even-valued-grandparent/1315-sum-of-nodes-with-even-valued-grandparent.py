# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:                
        stack = [root]
        
        parent = {root: None}        
        
        nodes_sum = 0                
        
        while stack:
            current = stack.pop() 
            
            myparent = parent[current]
            
            if myparent:
                mygrandparent = parent[myparent]
            
                if mygrandparent and mygrandparent.val % 2 == 0:
                    nodes_sum += current.val
            
            if current.left:
                parent[current.left] = current                                
                stack.append(current.left)
            
            if current.right:
                parent[current.right] = current
                stack.append(current.right)
                
        return nodes_sum
            
            
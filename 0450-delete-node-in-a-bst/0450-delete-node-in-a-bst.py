# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root):
        while root.left:
            root = root.left
            
        return root
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
                
        elif root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left
            
            minNode = self.findMinNode(root.right)
            
            # swap current node with the min node of right sub tree (inorder successor)
            root.val = minNode.val
            
            # find the minNode and delete it from the right sub tree
            root.right = self.deleteNode(root.right, minNode.val)
            
        
        return root
            
            
            
            
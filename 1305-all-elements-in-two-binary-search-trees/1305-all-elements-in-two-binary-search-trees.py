# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, elements):
            if not root:
                return
            
            self.traverse(root.left, elements)            
            
            elements.append(root.val)            
            
            self.traverse(root.right, elements)
        
        
    def merge(self, arr1, arr2):
        len_1 = len(arr1)
        len_2 = len(arr2)
        p1 = 0
        p2 = 0
        
        arr = []
        
        while p1 < len_1 and p2 < len_2:
            if arr1[p1] < arr2[p2]:
                arr.append(arr1[p1])
                p1 += 1
            
            else:
                arr.append(arr2[p2])
                p2 += 1
        
        arr.extend(arr1[p1:])
        arr.extend(arr2[p2:])
        
        return arr
        
        
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        elements_1 = []
        elements_2 = []
                
        self.traverse(root1, elements_1)
        self.traverse(root2, elements_2)
        
        return self.merge(elements_1, elements_2)
            
            
            
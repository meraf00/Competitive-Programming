# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []    
        self.current = root

    def next(self) -> int:
        while True:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            
            elif self.stack:
                node = self.stack.pop()
                self.current = node.right
                return node.val
            
            else:
                break
                    
    def hasNext(self) -> bool:
        return bool(self.stack) or bool(self.current)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
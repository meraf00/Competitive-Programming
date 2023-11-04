# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        index = {}
        max_index = 0
        
        def traverse(root, i):
            nonlocal max_index
            
            if not root:
                return
            
            max_index = max(max_index, i)
            index[i] = root.val
            
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            
            traverse(root.left, left_index)
            traverse(root.right, right_index)
            
        traverse(root, 0)
        
        serialized = []
        
        for k in sorted(index.keys()):
            serialized.append(str(k) + ':' + str(index[k]))
        
        return ','.join(serialized)            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        tree = data.split(',') 
        
        node_index = {}
        
        for node in tree:
            i, v = node.split(':')
            i = int(i)
            v = int(v)
            node_index[i] = v
            
        
        def build(root_idx):
            if root_idx not in node_index:
                return
            
            val = node_index[root_idx]

            node = TreeNode(int(val))
            
            left_index = 2 * root_idx + 1
            right_index = 2 * root_idx + 2
            
            left_child = build(left_index)
            right_child = build(right_index)
            
            node.left = left_child
            node.right = right_child
            
            return node
            
        return build(0)
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
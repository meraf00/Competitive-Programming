# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_info = {}
        
        # [(max height, max_contributer_node), (2nd max height, 2nd max contributer node)]
        level_info = defaultdict(lambda : [(-inf, None), (-inf, None)])
        
        def tree_height(node, level):
            if not node:
                return -1
            
            lh = tree_height(node.left, level + 1)
            rh = tree_height(node.right, level + 1)
            
            height = max(lh, rh) + 1
            
            node_info[node.val] = (height, level)            
            
            lvl = level_info[level]
            
            lvl.append((height, node.val))
            lvl.sort(reverse=True)
            lvl.pop()            
            
            return height
                
        T = tree_height(root, 0)
        
        # print(level_info)
        # print()
        # print(node_info)
        # print(T)
        result = []
        
        for node in queries:
            h, l = node_info[node]
            
            critical_nodes = level_info[l]
            
            if node == critical_nodes[0][1]:
                is_critical = True
                next_node = critical_nodes[1][1]
                next_node_contribution = critical_nodes[1][0]
            
            else:
                is_critical = False
                            
                       
            if is_critical:
                # the critical node is the only node in the level
                if next_node == None:
                    result.append(T - h - 1)
                
                else:
                    result.append(T - h + next_node_contribution)
            
            else:
                result.append(T)
                                    
        return result
                
            
            
            
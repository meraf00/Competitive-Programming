class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:        
        tree = defaultdict(list)
        
        for child, node in enumerate(parent):
            if node == -1:
                continue
            tree[node].append(child)  
        
        
        longest = 1
        
        def longest_path(node):                        
            nonlocal longest
                        
            best_subtree = 0
            second_best_subtree = 0
            
            for child in tree[node]:
                subtree = longest_path(child)                                
                
                if s[child] != s[node]:                                        
                    if subtree > best_subtree:                    
                        second_best_subtree = best_subtree
                        best_subtree = subtree
                    
                    elif subtree > second_best_subtree:
                        second_best_subtree = subtree
              
            # if longest path uses current node as turning point
            longest = max(longest, 1 + best_subtree + second_best_subtree)
            
            # if longest path doesn't use current node as turning point
            return 1 + best_subtree
    
        longest_path(0)
        
        return longest
                
                        
        
    
        
            
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)                
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
            
        
        def dfs(root, visited):  
            visited.add(root)
            
            if not tree[root]:
                if values[root] % k == 0:
                    return 0, 1
                
                return values[root], 0
            
            count = 0
            component_sum = values[root]
            
            for child in tree[root]:
                if child not in visited:
                    child_sum, child_count = dfs(child, visited)

                    component_sum += child_sum
                    count += child_count
            
            if component_sum % k == 0:
                return 0, count + 1
                
            return component_sum, count                 
                
        visited = set()
        s, c = dfs(0, visited)                
        
        return c
        
        
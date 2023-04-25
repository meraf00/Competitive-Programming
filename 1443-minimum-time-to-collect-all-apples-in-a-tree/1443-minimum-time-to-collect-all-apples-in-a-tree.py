class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        
        time_count = 0
        
        def dfs(node, visited=None):                        
            nonlocal time_count
            
            if visited == None:
                visited = set()
                
            visited.add(node)
            
            fruitful = hasApple[node]
            
            for nbr in tree[node]:
                if nbr in visited:
                    continue
                    
                is_child_fruitful = dfs(nbr, visited)
                
                if is_child_fruitful:
                    time_count += 1
                    
                fruitful = is_child_fruitful or fruitful                        
                
            return fruitful
        
        dfs(0)
        
        return time_count * 2
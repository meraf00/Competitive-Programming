class Solution:
    def get_neighbours(self, bomb_idx, bombs):
        x0, y0, r0 = bombs[bomb_idx]                        

        for bomb2_idx in range(len(bombs)):
            if bomb_idx == bomb2_idx:
                continue

            x, y, r = bombs[bomb2_idx]

            if (x0 - x) ** 2 + (y0 - y) ** 2 <= r0 ** 2:
                yield bomb2_idx
                
                
    def maximumDetonation(self, bombs: List[List[int]]) -> int:                                            
        bombs = list(map(tuple, bombs))
        n_bombs = len(bombs)
        
        graph = defaultdict(list)
        
        for idx in range(n_bombs):
            graph[idx].extend(self.get_neighbours(idx, bombs))            

        
        max_count = 0
        
        for bomb_idx in range(n_bombs):
                
            stack = [bomb_idx]
            
            count = 0
            
            visited = set()
            
            while stack:                
                current  = stack.pop()
                
                if current in visited:
                    continue
                                
                visited.add(current) 
                
                count += 1                                
                
                for nbr in graph[current]:
                    if nbr not in visited:                        
                        stack.append(nbr)
            
            max_count = max(count, max_count)
                                
        return max_count
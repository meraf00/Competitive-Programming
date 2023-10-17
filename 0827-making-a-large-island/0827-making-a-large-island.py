class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
                
        reps = {i:i for i in range(n * n)}
        
        ranks = {i: grid[i // n][i % n] for i in range(n * n)}
        
        def find(member):
            root = member            
            while reps[root] != root:
                root = reps[root]                
                                      
            while reps[member] != root:
                parent = reps[member]
                reps[parent] = root
                member = parent
            
            return root
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
                        
            if xRep == yRep:
                return
            
            if ranks[xRep] > ranks[yRep]:
                reps[yRep] = xRep
                ranks[xRep] += ranks[yRep]
            
            else:
                reps[xRep] = yRep
                ranks[yRep] += ranks[xRep]
        
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < n and 0 <= new_col < n:
                    nbrs.append((new_row, new_col))
            
            return nbrs
        
        for row in range(n):
            for col in range(n):
                i = row * n + col
                
                if grid[row][col] == 0:
                    continue
                    
                for r, c in get_nbrs(row, col):
                    j = r * n + c
                    
                    if grid[r][c] == 0:
                        continue
                        
                    union(i, j)
        
        
        largest_island = max(ranks.values())
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    
                    nbr_reps = set()
                    size = 1
                    
                    for r, c in get_nbrs(row, col):
                        i = r * n + c
                        rep = find(i)
                        
                        if rep not in nbr_reps:
                            size += ranks[rep]
                            nbr_reps.add(rep)
                        
                    largest_island = max(largest_island, size)

        return largest_island
                
                
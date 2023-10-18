class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        
        reps = [i for i in range(rows * cols)]
        ranks = [grid[i // cols][i % cols] == '1' for i in range(rows * cols)]
        
        
        def find(member):
            root = member
            
            while reps[root] != root:
                root = reps[root]
            
            
            while reps[member] != root:
                parent = reps[member]
                reps[member] = root
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
        
        
        directions = [
            (0, 1), (1, 0), (-1, 0), (0, -1)
        ]
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                    nbrs.append(new_row * cols + new_col)
            
            return nbrs
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]  == "1":
                    for nbr in get_nbrs(row, col):
                        union(row * cols + col, nbr)
        
        
        unique_islands = set()
    
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]  == "1":
                    unique_islands.add(find(row * cols + col))
        
        return len(unique_islands)
                        
                        
        
        
        
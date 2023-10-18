class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        EDGE = rows * cols
        
        reps = [i for i in range(rows * cols + 1)]
        ranks = [grid[i // cols][i % cols] == '1' for i in range(rows * cols)]
        
        # rank for edge
        ranks.append(1)        
        
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
            
            edge = False
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == 1:
                        nbrs.append(new_row * cols + new_col)                
                else:
                    edge = True                    
            
            if edge:
                nbrs.append(EDGE)
                
            return nbrs
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]  == 1:
                    for nbr in get_nbrs(row, col):
                        union(row * cols + col, nbr)
            
        
        edge_rep = find(EDGE)
        
        count = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]  == 1:
                    if find(row * cols + col) != edge_rep:
                        count += 1
        
        return count
                        
                        
        
        
        
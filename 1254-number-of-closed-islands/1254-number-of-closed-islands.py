class DSU:
    def __init__(self, size):
        self.reps = {i: i for i in range(size)}
        self.rank = {i: i for i in range(size)}
        self.edge = defaultdict(lambda: False)
    
    def find(self, member):
        root = member
        while root != self.reps[root]:
            root = self.reps[root]
        
        
        while member != root:
            parent = self.reps[member]
            self.reps[member] = root
            member = parent
        
        return root
    
    
    def union(self, x, y, edge):
        xRep = self.find(x)
        yRep = self.find(y)
        
        self.edge[xRep] = edge or self.edge[xRep] or self.edge[yRep]
        self.edge[yRep] = edge or self.edge[xRep] or self.edge[yRep]
        
        if xRep == yRep:
            return                
        
        if self.rank[xRep] >= self.rank[yRep]:
            self.reps[yRep] = xRep
            self.rank[xRep] += self.rank[yRep]
            
        
        else:
            self.reps[xRep] = yRep
            self.rank[yRep] += self.rank[xRep]
            
        

class Solution:
    def flat_idx(self, row, col):
        return row * self.cols + col
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        dsu = DSU(self.rows * self.cols)
        
        directions = (
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        )
        
        def land_neighbours(row, col):
            nbrs = []
                        
            for dx, dy in directions:
                nbr_row = row + dy
                nbr_col = col + dx
                
                if 0 <= nbr_row < self.rows and 0 <= nbr_col < self.cols:
                    if grid[nbr_row][nbr_col] == 0:
                        nbrs.append((nbr_row, nbr_col))    
            
            return nbrs
    
        def is_edge(row, col):
            return row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1
                
        
        for row in range(self.rows):
            for col in range(self.cols):                                
                if grid[row][col] == 0:
                    dsu.union(self.flat_idx(row, col), self.flat_idx(row, col), is_edge(row, col))
                    for nbr in land_neighbours(row, col):                        
                        dsu.union(self.flat_idx(row, col), self.flat_idx(*nbr), is_edge(row, col))
        
        unique_reps = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    continue
                    
                rep = dsu.find(self.flat_idx(row, col))
                if not dsu.edge[rep]:
                    unique_reps.add(rep)
        
        
        return len(unique_reps)

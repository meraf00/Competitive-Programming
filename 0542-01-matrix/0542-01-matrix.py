class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:                
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        rows = len(mat)
        cols = len(mat[0])
        
        def get_neighbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows  and 0 <= new_col < cols:
                    neighbours.append((new_row, new_col))
            
            return neighbours
        
        
        ans = [[float('inf')] * cols for _ in range(rows)]        
        zeros = []
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:                    
                    ans[row][col] = 0
                    zeros.append((row, col))
        
        
        for zero in zeros:            
            for nbr in get_neighbours(zero):
                r, c = nbr
                if mat[r][c] == 1:
                    ans[r][c] = 1
        
        
        queue = deque()
        
        for row in range(rows):
            for col in range(cols):
                if ans[row][col] == 1:
                    queue.append((row, col))
            
        while queue :                
            node = queue.popleft()

            current_row, current_col = node

            for nbr in get_neighbours(node):
                r, c = nbr

                # not visited
                if ans[r][c] == float('inf'):
                    ans[r][c] = ans[current_row][current_col] + 1
                    queue.append(nbr)                
        
        return ans
              
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        
        
        directions = [
            ( 1,  0),
            ( 0,  1),
            (-1,  0),            
            ( 0, -1)
        ]
                                
        position = [0, 0]
        
        row_start = 0
        row_end = n
        col_start = -1
        col_end = n
        
        current_direction = RIGHT
        
        for i in range(n**2):              
            x, y = position
            
            grid[y][x] = i + 1
            
            dx, dy = directions[current_direction]            
            position[0] += dx
            position[1] += dy
            
            if current_direction == RIGHT:
                if position[0] >= col_end:
                    current_direction = DOWN
                    position[0] -= 1
                    position[1] += 1
                    col_end -= 1
            
            elif current_direction == DOWN:
                if position[1] >= row_end:
                    current_direction = LEFT
                    position[1] -= 1
                    position[0] -= 1                    
                    row_end -= 1
            
            elif current_direction == LEFT:
                if position[0] <= col_start:
                    current_direction = UP
                    position[0] += 1                    
                    position[1] -= 1
                    col_start += 1
            
            elif current_direction == UP:
                if position[1] <= row_start:
                    current_direction = RIGHT
                    position[1] += 1
                    position[0] += 1                    
                    row_start += 1
            
            
                                        
        return grid         
        
        
                
                
                
                
                
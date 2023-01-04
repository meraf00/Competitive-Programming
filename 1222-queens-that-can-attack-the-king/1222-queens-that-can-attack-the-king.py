class Solution:    
    def move(self, initial_position: List[int], direction: List[int], queens) -> Optional[List]:
        x0 = initial_position[0]
        y0 = initial_position[1]
        dx = direction[0]
        dy = direction[1]
        
        while 0 <= x0 <= 7 and 0 <= y0 <= 7:
            x0 += dx
            y0 += dy
            
            if [x0, y0] in queens:
                return [x0, y0]
        
        return None
            
        
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
                        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [-1, 1],[1, -1]]
        
        attacking_queens = []
        
        for direction in directions:    
            attacking_queen = self.move(king, direction, queens)
            if attacking_queen:
                attacking_queens.append(attacking_queen)
        
        return attacking_queens
            
            
            
        
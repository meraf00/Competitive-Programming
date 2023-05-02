class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:                        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        def to_number(board):            
            number = 0
            for i, num in enumerate(board[0]):
                number += num * 10 ** (5 - i)
            
            for i, num in enumerate(board[1]):
                number += num * 10 ** (2 - i)
            
            return number
        
        
        def get_next_state(board):                        
            # find empty cell
            found = False
            for row in range(2):
                for col in range(3):
                    if board[row][col] == 0:
                        found = True
                        break
                if found:
                    break
            
            neighbours = []                        
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    next_state = [r.copy() for r in board]
                    next_state[new_row][new_col], next_state[row][col] = next_state[row][col], next_state[new_row][new_col]
                    neighbours.append(next_state)
            
            return neighbours
                            
        
        target = to_number([[1,2,3], [4,5,0]])
        
        if to_number(board) == target:
            return 0
        
        visited = set([to_number(board)])
        
        queue = deque([(board, 0)])
        
        while queue:
            current, steps = queue.popleft()                        
            
            for next_state in get_next_state(current):
                state_hash = to_number(next_state)
                
                if state_hash == target:
                    return steps + 1
                
                if state_hash not in visited:
                    queue.append((next_state, steps + 1))
                    visited.add(state_hash)
                                        
        return -1
        
        
        
        
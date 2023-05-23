class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        def valid_state(state):
            for i in range(n): 
                x0, y0 = i, state[i]
                for j in range(i + 1, n):
                    x1, y1 = j, state[j]
                    
                    if x1 == x0 or y1 == y0 or abs((y0 - y1) / (x0 - x1)) == 1:
                        return False
            
            return True                                            
                              
        
        def mapper(state):
            board = [["."] * n for _ in range(n)]
            
            for row, col in enumerate(state):
                board[col][row] = "Q"
            
            
            return ["".join(row) for row in board]
            
        
        solutions = []        
        
        def backtrack(state, i, taken):            
            if len(state) == len(set(state)) and valid_state(state):
                solutions.append(mapper(state))
                                        
            
            for i in range(i, n):
                
                init = state[i]
                
                for j in range(init + 1, n):   
                    
                    if j in taken:
                        continue
                        
                    state[i] = j                    
                    taken.add(j)
                    
                    backtrack(state, i + 1, taken)
                    
                    state[i] = init
                    taken.discard(j)

        init_state = [0] * n
        
        backtrack(init_state, 0, set(init_state))
                
        return solutions
            
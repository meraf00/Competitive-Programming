class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(map(int, deadends))        
        
        target = int(target)
        
        def get_neighbours(state):
            
            neighbours = []
            
            for i in range(1, 5): 
                n = state
                
                ith_digit = 0
                for j in range(i):
                    ith_digit = n % 10
                    n //= 10                                    
                                
                # turn ith digit (wheel)
                turn_up = (ith_digit + 1) % 10
                turn_down = (ith_digit - 1) % 10                                
                    
                
                prefix = n
                suffix = ith_digit * 10 ** (i - 1)
                rest = state - n * 10 ** i - suffix
                
   
                
                candidate_1 = prefix * 10 ** i + turn_down * 10 ** (i - 1) + rest
                candidate_2 = prefix * 10 ** i + turn_up * 10 ** (i - 1) + rest
            
                            
                if candidate_1 not in deadends:
                    neighbours.append(candidate_1)
                
                if candidate_2 not in deadends:
                    neighbours.append(candidate_2)
                    
            
            return neighbours
        
        
                
        queue = deque([(0, 0)])        
        
        visited = set()
        
        while queue:            
            state, steps = queue.popleft()  
            
            if state in deadends:
                return -1
            
            if state == target:
                return steps
            
            for next_state in get_neighbours(state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
                            
        return -1
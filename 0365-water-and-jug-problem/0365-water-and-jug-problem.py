class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def get_nbrs(a, b):
            return [
                (max(a - jug2Capacity + b, 0), min(b + a, jug2Capacity)),
                (min(a + b, jug1Capacity), max(b - jug1Capacity + a, 0)),
                (0, 0),
                (jug1Capacity, b),
                (a, jug2Capacity),
                (0, b),
                (a, 0)
            ]                        
        
        stack = deque([(0, 0)])
        
        visited = set([(0, 0)])
        
        while stack:            
            current = stack.popleft()
            
            j1, j2 = current
            
            if j1 == targetCapacity or j2 == targetCapacity or j1 + j2 == targetCapacity:
                return True                        
                        
            for nbr in get_nbrs(j1, j2):
                if nbr not in visited: 
                    visited.add(nbr)
                    stack.append(nbr)
            
        return False
            
            
            
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        
        queue = deque([0])
        
        while queue:
            current = queue.popleft()
            
            
            for nbr in rooms[current]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        
        if len(visited) == len(rooms):
            return True
        
        return False
            
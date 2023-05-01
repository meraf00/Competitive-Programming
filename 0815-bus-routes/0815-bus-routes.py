class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:             
        if source == target:
            return 0
        
        
        n_buses = len(routes)
        
        routes = list(map(set, routes))
                
        # connected buses (if two buses share city they are connected)
        graph = defaultdict(list)
                
        
        for bus1, route1 in enumerate(routes):
            for bus2 in range(bus1 + 1, n_buses):
                route2 = routes[bus2]
                
                for city in route1:
                    if city in route2:
                        graph[bus1].append(bus2)
                        graph[bus2].append(bus1)
                        break
        
        visited = set()
        
        queue = deque()
        
        # list of buses we can take from source city
        for bus, route in enumerate(routes):
            if source in route:
                visited.add(bus)
                queue.append((bus, 1))
                
        
        while queue:
            current_bus, bus_count = queue.popleft()
            
            if target in routes[current_bus]:
                return bus_count
            
            for next_bus in graph[current_bus]:
                if next_bus not in visited:
                    queue.append((next_bus, bus_count + 1))
                    visited.add(next_bus)            
        
        return -1
            

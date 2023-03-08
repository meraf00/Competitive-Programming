class Solution:
    def time(self, pos, speed, target):
        distance_left = target - pos
            
        time_left = distance_left / speed
        
        return time_left    
    
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        
        for pos, speed in sorted(zip(position, speed)):
            times.append(self.time(pos, speed, target))
        
        
        slowest_time = 0
        
        fleet_count = 0
        
        for time in reversed(times):
            if time > slowest_time:
                fleet_count += 1
                slowest_time = time
        
        return fleet_count
    
            
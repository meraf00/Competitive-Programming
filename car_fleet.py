from  typing import List

class Solution:
    def time(self, pos, speed, target):
        distance_left = target - pos
            
        time_left = distance_left / speed
        
        return time_left
    
    
    def calculate_rendezvous(self, car1, car2):        
        pos_1, speed_1 = car1
        pos_2, speed_2 = car2
        
        if pos_1 == pos_2:
            return (0, pos_1)
        
        if pos_1 != pos_2 and speed_1 <= speed_2:
            return (0, -1)
        
        
        # car_1 and car_2 will meet at time t and distance d
        t = (pos_2 - pos_1) / (speed_1 - speed_2)                
        
        d = t * speed_1 + pos_1
        
        
        return (t, d)
        
    
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # contains (position, speed) tuple in decreasing order of time to destination
        stack = []
        
        
        # sort cars by position
        cars = list(zip(position, speed))
        cars.sort()
        
        
        time_passed = 0
                
        for pos, speed in cars:
            
            pos = pos + speed * time_passed
            
            while stack and self.time(*stack[-1], target) <= self.time(pos, speed, target):        
                pos_1, speed_1 = stack.pop()
                                
                time_elapsed, meet_pos = self.calculate_rendezvous((pos_1, speed_1), (pos, speed))
                
                if meet_pos > target or meet_pos == -1:
                    continue
                
                fleet_speed = min(speed_1, speed)
                
                pos, speed = meet_pos, fleet_speed
                
                time_passed += time_elapsed
                            
            stack.append((pos, speed))

        return len(stack) 
                
                               
# Solution().carFleet(31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4])
print(Solution().carFleet(21,[1,15,6,8,18,14,16,2,19,17,3,20,5],[8,5,5,7,10,10,7,9,3,4,4,10,2]))
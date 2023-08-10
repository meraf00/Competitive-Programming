class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters_count = len(heaters)
        
        heaters.sort()
        
        houses.sort()
                
        right = 0        
        
        max_radius = float('-inf')
        
        for house_pos in houses:
            while right < heaters_count:
                if heaters[right] >= house_pos:
                    break
                right += 1
            
            if right >= heaters_count:
                heater_right = float('inf')                
                heater_left = heaters[-1]
            
            elif right == 0:
                heater_left = float('inf')
                heater_right = heaters[0]
                
            else:
                heater_left = heaters[right - 1]
                heater_right = heaters[right]
            
            distance_1 = abs(house_pos - heater_left)
            distance_2 = abs(heater_right - house_pos)
            
            best_distance = min(distance_1, distance_2)
                        
            max_radius = max(max_radius, best_distance)
    
        return max_radius
            
            
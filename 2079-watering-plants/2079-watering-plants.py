class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n_plants = len(plants)
        
        current = 0
        
        steps = 0
        
        pos = 0
        
        count  = 0
        while pos < n_plants:
            current += plants[pos]
            
            if current > capacity:
                steps += 2 * pos
                current = 0                
                continue
            
            steps += 1
            pos += 1                
        
        return steps
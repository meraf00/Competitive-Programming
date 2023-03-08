class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        final_distance = max(trips, key=lambda x: x[-1])[-1]
        
        array = [0] * (final_distance + 2)
        
        for passengers, from_, to in trips:
            # early exit if passengers > capacity
            if passengers > capacity:
                return False
            
            array[from_] += passengers
            array[to] -= passengers                        
        

        # prefix sum
        for i in range(1, final_distance):
            array[i] += array[i - 1]

            if array[i] > capacity:
                return False
        
        return True
        
        
        
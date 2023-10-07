class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        n_stations = len(gas)
        
        total_gas = 0
        
        current_gas = 0
        
        for i in range(n_stations):
            total_gas += gas[i] - cost[i]
            
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        if total_gas < 0 or start >= n_stations:
            return -1
    
        return start
            
            
            
        
        
        
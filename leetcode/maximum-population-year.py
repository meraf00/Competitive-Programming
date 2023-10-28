class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = 2050 - 1950 + 2               
        
        prefix = [0] * (years)
        
        for birth, death in logs:            
            prefix[birth - 1949] += 1
            prefix[death - 1949] -= 1
        
        
        max_population = 0
        
        earliest_year = 0
        
        for i in range(1, years):
            prefix[i] += prefix[i - 1]
            
            if prefix[i] > max_population:
                max_population = prefix[i]
                earliest_year = i
        
        return earliest_year + 1949
        
                
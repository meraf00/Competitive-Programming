class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost_difference = []
        
        for index, c in enumerate(costs):
            cost_a, cost_b = c
            
            cost_difference.append((cost_a - cost_b, index))
            
        cost_difference.sort()
        
        total_cost = 0
        
        n = len(costs) // 2
        
        counter = 0
        
        for _, person_index in cost_difference:
            # first half of the list goes to city a
            if counter < n:
                total_cost += costs[person_index][0]
                counter += 1                                
            
            # second half of the list goes to city b
            else:
                total_cost += costs[person_index][1]                            
            
            
        return total_cost
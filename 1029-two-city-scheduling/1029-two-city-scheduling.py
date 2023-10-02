class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by cost difference
        costs.sort(key = lambda x: x[0] - x[1])
        
        n_people = len(costs)
        
        half_people = n_people // 2
                
        min_cost = 0
        
        for i in range(n_people):
            if i < half_people:
                min_cost += costs[i][0]
            
            else:
                min_cost += costs[i][1]
        
        return min_cost
                
            
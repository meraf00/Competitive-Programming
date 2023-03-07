class Solution:
    def calculate_days(self, weights, capacity):        
        n_weights = len(weights)
        
        days = 0
        
        i = 0
        
        current_capacity = capacity
        
        while i < n_weights:
            while i < n_weights and current_capacity >= weights[i]:
                current_capacity -= weights[i]
                i += 1
                
            days += 1
            current_capacity = capacity
            
        return days
            
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n_weights = len(weights)
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = (low + high) // 2
            
            days_required = self.calculate_days(weights, mid)
            
            if days_required <= days:
                high = mid - 1                
            
            else:
                low = mid + 1                
        
        return low
            
                
        
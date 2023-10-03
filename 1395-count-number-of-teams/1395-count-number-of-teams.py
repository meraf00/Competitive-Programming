class Solution:    
    def numTeams(self, rating: List[int]) -> int:
        length =  len(rating)
        
        less_before = [0] * length         
        less_after = [0] * length  
        greater_before = [0] * length
        greater_after = [0] * length
        
        for i in range(length):
            for j in range(length):                
                if i < j:
                    if rating[i] < rating[j]:
                        less_before[j] += 1  
                        greater_after[i] += 1
                
                    if rating[i] > rating[j]:
                        less_after[i] += 1
                        greater_before[j] += 1
                                        
            
        increasing_count = 0
        
        for left_possible, right_possible in zip(less_before, greater_after):
            increasing_count += left_possible * right_possible
        
        
        decreasing_count = 0
        
        for left_possible, right_possible in zip(greater_before, less_after):
            decreasing_count += left_possible * right_possible
        
        
        return increasing_count + decreasing_count
    
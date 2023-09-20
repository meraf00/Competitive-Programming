class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n_foods = len(satisfaction)
        
        satisfaction.sort(reverse=True)
        
        for i in range(1, n_foods):
            satisfaction[i] += satisfaction[i - 1]
        
        total_satisfaction = 0
        
        for n in satisfaction:
            if n < 0:
                break
            
            total_satisfaction += n
        
        return total_satisfaction
        
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:        
        
        queue_length = len(tickets)
        
        i = 0
        
        time = 0
        
        while tickets[k] > 0:
            
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
            
            i = (i + 1) % queue_length
        
        return time
        
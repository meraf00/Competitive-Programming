class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [n for n in amount if n != 0]
        
        for i in range(len(amount)):
            amount[i] *= -1
                    
        heapify(amount)
        
        count = 0
        
        while len(amount) == 3:
            a = heappop(amount)
            b = heappop(amount)                        
            
            if a + 1 < 0:
                heappush(amount, a + 1)
                
            if b + 1 < 0:
                heappush(amount, b + 1)
            
            count += 1
                                
        if amount:
            count += -min(amount)
        
        return count
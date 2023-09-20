class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = list(map(lambda x:-x, cost))
        
        heapify(cost)
        
        total = 0
        
        while len(cost) > 2:
            a = -heappop(cost)
            b = -heappop(cost)
            heappop(cost)
            
            total += a + b
            
        total += -sum(cost)
        
        return total
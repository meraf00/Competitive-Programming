class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
                    
        heapify(stones)
        
        while len(stones) > 1:
            y = -1 * heappop(stones)
            x = -1 * heappop(stones)
            
            if x != y:
                heappush(stones, x - y)
        
        if stones:
            return -1 * stones[0]
        
        return 0
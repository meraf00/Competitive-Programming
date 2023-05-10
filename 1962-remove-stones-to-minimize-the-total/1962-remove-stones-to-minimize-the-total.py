class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i, stone in enumerate(piles):
            piles[i] = -stone
            
        heapify(piles)
        
        while k:
            stone = -heappop(piles)
            stone -= stone // 2
            heappush(piles, -stone)
            
            k -= 1
    
        return -sum(piles)
        
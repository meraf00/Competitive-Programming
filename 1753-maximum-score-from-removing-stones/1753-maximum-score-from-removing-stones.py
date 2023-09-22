class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = [-a, -b, -c]
        
        max_score = 0
        
        while True:
            a = heappop(piles)
            b = heappop(piles)
            
            if a == 0 or b == 0:
                break
                
            heappush(piles, a + 1)
            heappush(piles, b + 1)
            
            max_score += 1
        
        return max_score
            
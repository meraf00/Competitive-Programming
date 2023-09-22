class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapify(gifts)
                
        for _ in range(k):
            n = -heappop(gifts)
            
            if n == 0:
                break
                
            left = int(sqrt(n))
            
            heappush(gifts, -left)
        
        return -sum(gifts)
            
            
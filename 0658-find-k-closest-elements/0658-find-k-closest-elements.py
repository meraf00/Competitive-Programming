class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_closest = []
        
        for num in arr:
            heappush(k_closest, (-abs(num - x), -num))
            
            if len(k_closest) > k:
                heappop(k_closest)
        
        for i in range(len(k_closest)):
            k_closest[i] = -k_closest[i][1]
        
        k_closest.sort()
        
        return k_closest
        
        
            
        
        
        
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        k_smallest = []
        k_largest = []
        
        for i in range(1, len(weights)):
            pair_score = weights[i] + weights[i - 1]
            
            heappush(k_largest, pair_score)
            heappush(k_smallest, -pair_score)
            
            while len(k_largest) > k - 1:
                heappop(k_largest)
                heappop(k_smallest)
                        
        return  sum(k_largest) + sum(k_smallest)
        
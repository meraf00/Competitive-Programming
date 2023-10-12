class Solution:
    def countOrders(self, n: int) -> int:
        mod = pow(10, 9) + 7
        
        count = 1
        
        for i in range(n * 2 - 1, 0, -2):
            ways_to_place_p_d = i * (i + 1) // 2                        
            
            count *= ways_to_place_p_d
            
            count %= mod
            
        return count
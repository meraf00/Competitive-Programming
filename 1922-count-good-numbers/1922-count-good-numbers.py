class Solution:
    def countGoodNumbers(self, n: int) -> int:        
        mod = pow(10, 9) + 7
        
        odd_index_count = n // 2
        even_index_count = n // 2 + n % 2
        
        return (pow(5, even_index_count, mod) * pow(4, odd_index_count, mod)) % mod
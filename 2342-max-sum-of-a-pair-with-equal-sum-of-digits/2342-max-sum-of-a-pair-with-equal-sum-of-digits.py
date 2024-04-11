class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_indices = defaultdict(list)
        
        max_sum = -1
        
        for i, num in enumerate(nums):
            digits_sum = 0
            
            n = num
            while n != 0:
                digits_sum += n % 10
                n //= 10
                
            heappush(sum_indices[digits_sum], num)
            
            while len(sum_indices[digits_sum]) > 2:
                heappop(sum_indices[digits_sum])
            
            if len(sum_indices[digits_sum]) == 2:
                max_sum = max(max_sum, sum(sum_indices[digits_sum]))
        
        return max_sum
        
        
            
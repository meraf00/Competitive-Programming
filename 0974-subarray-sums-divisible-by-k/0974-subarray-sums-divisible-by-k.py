class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        
        current_sum = 0
        
        subarrays = 0
        
        for num in nums:
            current_sum += num
            
            remainder = current_sum % k
            
            if remainder == 0:
                subarrays += 1
            
            subarrays += counter[current_sum % k]
            
            counter[remainder] += 1                        
        
        return subarrays
            
        
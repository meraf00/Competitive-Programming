class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        
        running_sum = 0
        
        subarrays = 0
        
        for num in nums:
            running_sum += num
            
            if running_sum == goal:
                subarrays += 1
            
            subarrays += counter[running_sum - goal]
            
            counter[running_sum] += 1
        
        return subarrays
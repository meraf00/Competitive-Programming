class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:                
        prefix_sum = [nums[0]] * len(nums)
        
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]
            
        left = 0
        subarray_count = 0
        counter = {}
        
        for i in range(len(nums)):
            if prefix_sum[i] - k in counter:
                subarray_count += counter[prefix_sum[i] - k]
                
            if prefix_sum[i] == k:
                subarray_count += 1
            
            if counter.get(prefix_sum[i]):
                counter[prefix_sum[i]] += 1
            else:
                counter[prefix_sum[i]] = 1
            
        return subarray_count
            
        
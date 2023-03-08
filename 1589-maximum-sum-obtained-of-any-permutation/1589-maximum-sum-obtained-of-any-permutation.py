class Solution:
    
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        query_freq = [0] * (len(nums) + 1)
        
        for start, end in requests:
            query_freq[start] += 1
            query_freq[end + 1] -= 1
        
        
        
        for i in range(1, len(nums)):
            query_freq[i] += query_freq[i - 1]
        
        query_freq.pop()
        
        query_freq.sort(reverse=True)
        
        nums.sort(reverse=True)
        
                
        max_sum = 0
        for num, freq in zip(nums, query_freq):
            if freq == 0: 
                break
            
            max_sum += freq * num

            
            
        return max_sum % 1_000_000_007
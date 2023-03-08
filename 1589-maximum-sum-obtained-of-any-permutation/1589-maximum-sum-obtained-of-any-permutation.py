class Solution:    
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
                
        prefix[0] = (-prefix[0], 0)        
                
        for i in range(1, len(nums)):
            val, _ = prefix[i - 1]
            prefix[i] = (val - prefix[i], i)
            
        prefix.pop()
        
        heapify(prefix)
        
        nums.sort(reverse=True)
                        
        largest_num_index = 0
        
        optimal_order = [0] * (len(nums))
        
        
        while prefix:
            _, index = heappop(prefix)
            
            optimal_order[index] = nums[largest_num_index]
            
            largest_num_index += 1
         
        for i in range(1, len(optimal_order)):
            optimal_order[i] += optimal_order[i - 1]
        
        optimal_order.append(0)
        
        max_sum  = 0
        for start, end in requests:
            
            max_sum += optimal_order[end] - optimal_order[start-1]
        
        
        return max_sum % 1_000_000_007
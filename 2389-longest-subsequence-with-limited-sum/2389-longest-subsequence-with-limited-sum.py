class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        # prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        
        answer = []
        for query in queries:
            idx = bisect_right(nums, query)
            answer.append(idx)
        
        return answer
            
        
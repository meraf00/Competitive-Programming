class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:                
        rows = len(nums)
        cols = len(nums[0])
        
        for row in nums:
            for i in range(cols):
                row[i] *= -1
                
            heapify(row)
        
        score = 0                
        
        for _ in range(cols):
            max_num = float('-inf')
            
            for row in nums:
                max_num = max(-heappop(row), max_num)
            
            score += max_num
        
        return score
            
                
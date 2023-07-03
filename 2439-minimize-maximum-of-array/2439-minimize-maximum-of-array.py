class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        answer = 0
        
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            i = i + 1
            answer = max(answer, (prefix_sum // i) + (prefix_sum % i != 0))
        
        return answer
        
        
# [3,7,1,6]
# [10,1]
# [13,13,20,0,8,9,9]
# [6,9,3,8,14]
# [4,7,2,2,9,19,16,0,3,15]         
            
            
        
        
                
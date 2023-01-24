class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_than_target = 0
        larger_than_target = 0
        equal_to_target = 0
        
        for num in nums:
            if num == target:
                equal_to_target += 1
            elif num < target:
                smaller_than_target += 1
            elif num > target:
                larger_than_target += 1
        
        answer = []
        for index in range(smaller_than_target, smaller_than_target + equal_to_target):
            answer.append(index)
        
        return answer
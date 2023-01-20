class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0] * 101
        
        for num in nums:
            counter[num] += 1
                
        # prefix sum on counter
        for index in range(1, 101):
            counter[index] = counter[index-1] + counter[index]
        
        for index, num in enumerate(nums):
            if num != 0:
                nums[index] = counter[num - 1]
            else:
                nums[index] = 0
        
        return nums
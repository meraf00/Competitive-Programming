class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) / 3
        
        nums.append(float('inf'))
        
        nums.sort()
        
        left = 0
        
        ans = []
        
        for right, num in enumerate(nums):
            if num != nums[left]:
                if (right - left) > target:
                    ans.append(nums[left])
                    
                left = right
            
        return ans
                
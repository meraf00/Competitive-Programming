class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        total = 0
        
        n_nums = len(nums)          
                
        for i, target in enumerate(nums):                        
            target *= -1    
                        
            seen = set()

            for j in range(i + 1, n_nums):
                num = nums[j]                                 
                
                if target - num in seen:
                        triplate = tuple(sorted([num, -target, target - num]))
                        ans.add(triplate)
                                
                seen.add(num)
                            
        return ans
class Solution:
    def countMissing(self, nums, idx):
        expected = nums[idx]
        return expected - (idx + 1)
    
    def findKthPositive(self, nums: List[int], k: int) -> int:          
        low = 0
        high = len(nums) - 1    

        while low < high:
            mid = (low + high) // 2

            if self.countMissing(nums, mid) < k:
                low = mid + 1                        

            else:
                high = mid - 1

        n_missing = self.countMissing(nums, high)                   
        
        if high < 0:
            return k
                
        if n_missing >= k:             
            return nums[high] + k - n_missing - 1
        
        return nums[high] + k - n_missing
    
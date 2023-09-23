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
    
    def findKthPositive_(self, arr: List[int], k: int) -> int:          
        number_of_missing_num = arr[0] - 1
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1] - 1

            number_of_missing_num += diff        

            if number_of_missing_num >= k:
                prev_missing = number_of_missing_num - diff
                offset = k - prev_missing      
                if offset <= 0:
                    offset -= 1
                return arr[i - 1] + offset
        
        if k == number_of_missing_num:
            k -= 1
            
        return arr[-1] - number_of_missing_num + k
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        nums.append(float('-inf'))
        
        
        while low <= high:
            mid = (low + high) // 2
            
            left = nums[mid - 1]
            right = nums[mid + 1]
            
            if nums[mid] > left and nums[mid] > right:
                return mid
            
            elif right > left:
                low = mid + 1
            
            else:
                high = mid - 1
        
        
        return mid
            
class Solution:
    def find(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return -1
    
    def locate(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return mid
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_index = self.find(nums, target)
        
        if target_index == -1:
            return [-1, -1]
        
        start = self.locate(nums, target - .5)
        end = self.locate(nums, target + .5)
        
        if nums[start] < target:
            start += 1
        
        if nums[end] > target:
            end -= 1
                    
        return [start, end]
        
        
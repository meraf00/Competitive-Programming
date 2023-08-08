class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2                          
            
            if nums[mid] > nums[-1]:
                low = mid + 1
            
            elif nums[mid] < nums[0]:
                high = mid - 1
            
            else:
                break
                            
        
        
        if target >= nums[0]:            
            low = 0
            
        else:
            high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2                          
            
            if nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] > target:
                high = mid - 1
            
            else:
                return mid
        
        return -1
                

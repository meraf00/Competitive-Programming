# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
                
        memo =  {}
        
        def get(idx):
            if idx in memo:
                return memo[idx]
            
            memo[idx] = mountain_arr.get(idx)
            
            return memo[idx]
        
        
        low = 1
        high = length - 2                
        mid = (low + high) // 2
        
        while low <= high:
            mid = (low + high) // 2
            
            left = get(mid - 1)
            right = get(mid + 1)
            
            if left < get(mid) < right:
                low = mid + 1
            
            elif left > get(mid) > right:
                high = mid - 1
            
            else:
                break                
        
        peak = mid
        
        low = 0
        high = peak - 1                
        
        while low <= high:
            mid = (low + high) // 2                        

            if get(mid) == target:
                return mid

            elif get(mid) < target:
                low = mid + 1                

            else:
                high = mid - 1
        
        if target == get(peak):
            return peak
        
        low = peak + 1
        high = length - 1

        while low <= high:
            mid = (low + high) // 2                        

            if get(mid) == target:
                return mid

            elif get(mid) > target:
                low = mid + 1                

            else:
                high = mid - 1                                      
        
        return -1
        

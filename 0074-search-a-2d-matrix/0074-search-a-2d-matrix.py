class Solution:  
    def binarySearch(self, array, target):
        low = 0
        high = len(array) - 1        
        mid = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if array[mid] < target:
                low = mid + 1
            
            elif array[mid] > target:
                high = mid - 1
            
            else:
                return True
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1        
        mid = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[mid][0] < target:
                low = mid + 1
            
            elif matrix[mid][0] > target:
                high = mid - 1
            
            else:
                return True
                
        check_inside_row = self.binarySearch(matrix[high], target)
        
        return check_inside_row
        
        
        
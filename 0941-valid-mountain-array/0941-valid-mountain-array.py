class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        array_length = len(arr)
        
        if array_length < 3:
            return False
        
        for i in range(array_length - 1):
            if arr[i] >= arr[i + 1] :
                break
        
        for j in range(array_length - 1, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
        
        if i == j:
            return True
        
        return False
        
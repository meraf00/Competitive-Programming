class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = arr[-1]
        arr[-1] = -1
        for right in range(len(arr)-2,-1,-1):
            new_max_element = max(arr[right], max_element)
            arr[right] = max_element
            max_element = new_max_element
        
        return arr
        
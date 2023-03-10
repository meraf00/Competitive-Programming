class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        low = 0
        high = len(citations)
             
            
        while low <= high:
            mid = (low + high) // 2
            
            if size - bisect_left(citations, mid) >= mid:
                low = mid + 1
            
            else:
                high = mid - 1

                
        return high
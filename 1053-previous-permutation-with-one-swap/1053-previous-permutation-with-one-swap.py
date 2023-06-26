class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # heap = [(-arr[-1], len(arr) - 1)]
        
        heap = []
        
        for i in range(len(arr) - 1, 0, -1):  
            heappush(heap, (-arr[i], i))
            
            if arr[i] < arr[i - 1]:                
                num, idx = heappop(heap)
                
                while heap and -num >= arr[i - 1]:
                    num, idx = heappop(heap)
                
                arr[i - 1], arr[idx] = arr[idx], arr[i - 1]
                
                break

        return arr


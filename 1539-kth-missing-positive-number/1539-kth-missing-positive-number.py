class Solution:    
    def findKthPositive(self, arr: List[int], k: int) -> int:          
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
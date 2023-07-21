class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        left = 0
        
        current_sum = 0
        
        count = 0
        
        for right, num in enumerate(arr):
            current_sum += num
            
            while right - left + 1 > k:
                current_sum -= arr[left]
                left += 1
            
            if right - left + 1 != k:
                continue
            
            average = current_sum / k            
            
            if average >= threshold:
                count += 1
            
        return count
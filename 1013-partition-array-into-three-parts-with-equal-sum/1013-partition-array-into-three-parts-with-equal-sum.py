class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)                
        
        if total % 3 != 0:
            return False                
        
        target = total // 3
        
        running_sum = 0
        
        partition_count = 0                
        
        for right in range(len(arr)):
            if partition_count == 2:
                return True
            
            running_sum += arr[right]
            
            if running_sum == target:
                running_sum = 0
                partition_count += 1    
        
        return False

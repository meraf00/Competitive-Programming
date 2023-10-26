class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = pow(10, 9) + 7
        
        n = len(arr)  
        
        arr.sort()
        
        nums = {n:i for i, n in enumerate(arr)}                
        
        ans = [1] * n
        
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] != 0:
                    continue
                    
                target = arr[i] // arr[j]
                
                if target in nums:                    
                    index = nums[target]                                        
                
                    ans[i] += ans[index] * ans[j]
     
        return sum(ans) % mod
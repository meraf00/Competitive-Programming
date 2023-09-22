class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:   
        n = len(arr)                
        
        @cache
        def dp(i, j):
            if i == j:
                return 0, arr[i]
            
            if j - i == 1:
                return arr[i] * arr[j], max(arr[i], arr[j])
            
            min_sum, max_num = float('inf'), 0
            
            for k in range(i, j):                                
                left_sum, left_max = dp(i, k)
                right_sum, right_max = dp(k + 1, j)

                temp = left_sum + right_sum + left_max * right_max
                
                if temp < min_sum:
                    min_sum = temp
                    max_num = max(left_max, right_max)
            
            return min_sum, max_num
        
        min_sum, _ = dp(0, n - 1)
        
        return min_sum
                
            
        
"""
[6,2,4]
[4,11]
[7,12,8,10]
[1,2,3,1,2,3]
[1,2,3,4,5]
[2,5,1,2,3,4]
[6,5,4,3,2,1]
[5,4,3,2,1]
[1,2,3,3,2,1]
[1,2,3,3,2,11,2,3]
"""     
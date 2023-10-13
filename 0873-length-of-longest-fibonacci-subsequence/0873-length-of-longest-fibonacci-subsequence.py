class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        
        num_to_index = {num: i for i, num in enumerate(arr)}
                        
        dp = [[2] * n for _ in range(n)]
        
        longest_subseq = 0
        
        for i in range(1, n):
            prev = arr[i]
            for j in range(1, n):
                curr = arr[j]                                
                
                prev_prev = curr - prev  
                                                
                if prev_prev < prev and prev_prev in num_to_index:
                    k = num_to_index[prev_prev]                                        
                    dp[i][j] = dp[k][i] + 1
                
                longest_subseq = max(longest_subseq, dp[i][j])  
                    
        if longest_subseq < 3:
            return 0
        
        return longest_subseq
                
                
                
                
            
"""
[1,2,3,4,5,6,7,8]
[1,3,7,11,12,14,18]
[1,2,3]
[1,2,5]
"""        
        
        
            
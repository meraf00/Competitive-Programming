class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        var_to_idx = {}
        
        for a, b in equations:
            if a not in var_to_idx:
                var_to_idx[a] = len(var_to_idx)
            
            if b not in var_to_idx:
                var_to_idx[b] = len(var_to_idx)
                   
        
        n_vars = len(var_to_idx)
        
        dp = [[float('inf')] * n_vars for _ in range(n_vars)]        
        
        for eq, val in zip(equations, values):
            a, b = eq
            
            a_idx = var_to_idx[a]
            b_idx = var_to_idx[b]
                        
            dp[a_idx][b_idx] = val
            
            if val != 0:
                dp[b_idx][a_idx] = 1 / val
                dp[a_idx][a_idx] = 1
                dp[b_idx][b_idx] = 1   
        
        
        for k in range(n_vars):
            for i in range(n_vars):
                for j in range(n_vars): 
                    if dp[i][j] == float('inf'):
                        dp[i][j] = dp[i][k] * dp[k][j]
                  
        
        results = []
        
        for a, b in queries:
            if a not in var_to_idx or b not in var_to_idx:
                results.append(-1)
                continue
                
            a_idx = var_to_idx[a]
            b_idx = var_to_idx[b]
            
            result = dp[a_idx][b_idx]                                  
            
            if result == float('inf'):
                results.append(-1)
                continue
                
            results.append(result)
            
        return results
    
"""

"""
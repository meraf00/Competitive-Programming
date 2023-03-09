class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        
        distribution = [0] * k
        
        def backtrack(cookie_index):
            nonlocal min_unfairness
            
            if cookie_index >= len(cookies):
                unfairness = max(distribution)
                
                min_unfairness = min(unfairness, min_unfairness)
                
                return
            
            
            for i in range(k):
                
                distribution[i] += cookies[cookie_index]
                
                if distribution[i] >= min_unfairness:
                    distribution[i] -= cookies[cookie_index]
                    continue
                
                backtrack(cookie_index + 1)
                
                distribution[i] -= cookies[cookie_index]
            
            
        backtrack(0)
        
        return min_unfairness
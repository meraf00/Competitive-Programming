class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        
        def backtrack(distribution, cookie_index):
            nonlocal min_unfairness
            
            if cookie_index >= len(cookies):
                unfairness = max(distribution)
                min_unfairness = min(unfairness, min_unfairness)
                
                return
            
            
            for i in range(k):
                distribution_copy = distribution[:]
                
                distribution_copy[i] += cookies[cookie_index]
                
                if distribution_copy[i] >= min_unfairness:
                    continue
                
                backtrack(distribution_copy, cookie_index + 1)
            
            
        backtrack([0] * k, 0)
        
        return min_unfairness
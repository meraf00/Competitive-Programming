class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project_poll = []
        
        for i, profit in enumerate(profits):
            profits[i] = (capital[i], profit)
        
        profits.sort()
        
        project_i = 0
        
        n = len(capital)
                
        while k > 0:            
            while project_i < n and profits[project_i][0] <= w:
                _, profit = profits[project_i]            
                heappush(project_poll, -profit)
                project_i += 1
            
            if not project_poll:
                break
                
            w += -heappop(project_poll)
            k -= 1
        
        return w
            
            
        
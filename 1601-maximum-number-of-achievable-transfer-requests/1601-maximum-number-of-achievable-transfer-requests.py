class Solution:
    def valid(self, buildings):
        for building in buildings.values():
            if building != 0:
                return False
        return True
    
    
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        buildings = defaultdict(int) 
        
        maximum_transfer = 0
        
        current_transfer = 0
        
        length = len(requests)
        
        def backtrack(start_idx):
            nonlocal maximum_transfer, current_transfer
            
            if self.valid(buildings):
                maximum_transfer = max(maximum_transfer, current_transfer)
                
            if start_idx >= length:
                return                         
            
            for i in range(start_idx, length):
                from_, to = requests[i]
                
                current_transfer += 1
                
                buildings[from_] -= 1
                buildings[to] += 1
                
                backtrack(i + 1)
                
                current_transfer -= 1
                
                buildings[from_] += 1
                buildings[to] -= 1
                                    
            
        backtrack(0)
        
        return maximum_transfer
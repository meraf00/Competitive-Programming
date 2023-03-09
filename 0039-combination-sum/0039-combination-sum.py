class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        current_combination = []
        
        def backtrack():
            if sum(current_combination) == target:
                combinations.append(current_combination[:])
                return
            
            for num in candidates:
                # to avoid duplicates only allow combinations in increasing order
                if current_combination and current_combination[-1] > num:
                    continue
                    
                current_combination.append(num)                                
                                
                if sum(current_combination) > target:
                    current_combination.pop()
                    continue
                
                backtrack()
                
                current_combination.pop()
        
        backtrack()
        
        return combinations
            
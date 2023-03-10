class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        subsets = [[]]
        
        current_subset = []
        
        def backtrack(start_index):
            if start_index >= length:
                return            
            
            for i in range(start_index, length):                                
                
                current_subset.append(nums[i])                
                
                subsets.append(current_subset[:])
                
                backtrack(i + 1)                
                
                current_subset.pop()
                                                                        
        
        backtrack(0)
        
        return subsets
                
                
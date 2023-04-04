class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise_or = reduce(lambda x, y: x | y, nums)        
        
        length = len(nums)
        
        count = 0  
        
        subset = set()
                
        def backtrack(start_index):                                    
            nonlocal count
            
            if len(subset):
                
                bitwise_or = 0
                for index in subset:
                    bitwise_or |= nums[index]
                
                if bitwise_or == max_bitwise_or:
                    count += 1
            
            if start_index == length:
                return
            
            for i in range(start_index, length):
                subset.add(i)
                
                backtrack(i + 1)
                
                subset.remove(i)
        
        
        backtrack(0)
        
        return count
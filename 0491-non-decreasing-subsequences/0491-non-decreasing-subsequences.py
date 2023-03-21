class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
                
        seq = []
        
        output = set()
        
        def backtrack(index):
            if index >= length:                
                return   
                        
                
            for i in range(index, length):
                seq.append(nums[i])
                
                if len(seq) >= 2 and seq[-1] < seq[-2]:
                    seq.pop()   
                    continue
                    
                if len(seq) >= 2:
                    output.add(tuple(seq))
                
                backtrack(i + 1)                                
                
                if seq:
                    seq.pop()            
                              
            
        backtrack(0)
        
        return list(map(list, output))
                    
                    
            
            
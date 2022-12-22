class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}               
        
        pair_counter = 0
        for d in deliciousness:
            for i in range(22):                 
                if count.get(2 ** i - d):                    
                    pair_counter += count.get(2 ** i - d)
            if count.get(d):
                count[d] += 1
            else:
                count[d] = 1
                              
        return pair_counter % (10**9 + 7)
                    
                
        
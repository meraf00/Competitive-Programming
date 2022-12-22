class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)                
        
        two_powers = []        
        
        pair_counter = 0
        for d in count.keys():
            for i in range(22):                
                if 2**i - d < d: continue
                
                if 2**i - d == d:
                    freq = count[d]
                    pair_counter += freq * (freq - 1) // 2
                    
                else:
                    pair_counter += count[d] * count[2**i - d]
                            
        return pair_counter % (10**9 + 7)
                    
                
        
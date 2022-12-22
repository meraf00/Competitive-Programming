class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)                
        
        two_powers = []
        
        for i in range(22):
            two_powers.append(2**i)
        
        pair_counter = 0
        for d in count.keys():
            for t in two_powers:                
                if t - d < d: continue
                
                if t - d == d:
                    freq = count[d]
                    pair_counter += freq * (freq - 1) // 2
                    
                else:
                    pair_counter += count[d] * count[t-d]
                            
        return pair_counter % (10**9 + 7)
                    
                
        
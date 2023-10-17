class Solution:
    def minimumOperations(self, nums: List[int]) -> int:        
        n = len(nums)           
        
        if n == 1:
            return 0
    
        
        freq_odd = defaultdict(int)
        freq_even = defaultdict(int)
                
        for i, num in enumerate(nums):
            if i & 1:
                freq_odd[num] += 1                                
            
            else:
                freq_even[num] += 1
        
        fodd = sorted([(f, i) for i, f in freq_odd.items()], reverse=True)
        feven = sorted([(f, i) for i, f in freq_even.items()], reverse=True)
                
        fo1, no1 = fodd[0]
        fo2, no2 = fodd[1] if 1 < len(fodd) else (float('-inf'), None)
        
        fe1, ne1 = feven[0]
        fe2, ne2 =  feven[1] if 1 < len(feven) else (float('-inf'), None)
        

        if no1 != ne1:            
            return n - fo1 - fe1
        
        
        return min(
            n - fo1,
            n - fe1,
            n - fo1 - fe2 if no1 != ne2 else float('inf'),
            n - fe1 - fo2 if ne1 != no2 else float('inf')
        )


       
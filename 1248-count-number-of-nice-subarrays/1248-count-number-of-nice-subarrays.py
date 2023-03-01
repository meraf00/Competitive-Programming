class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        counter = defaultdict(int)        
        
        odds = 0
        
        nice_arrays = 0
        
        for num in nums:
            if num % 2:
                odds += 1
            
            if odds == k:
                nice_arrays += 1
                        
            nice_arrays += counter[odds - k]
            
            counter[odds] += 1
        
        return nice_arrays
            
                
        
        
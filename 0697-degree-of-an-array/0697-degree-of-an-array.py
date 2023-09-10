class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        most_common = counter.most_common()
        
        candidates = set()
        
        for num, freq in most_common:
            if freq == most_common[0][1]:
                candidates.add(num)
        
        
        num_range = defaultdict(lambda: [None, None])
        
        
        for idx, num in enumerate(nums):            
            if num not in candidates:
                continue

            start, end = num_range[num]
            
            if start == None:
                num_range[num][0] = idx
                
            num_range[num][1] = idx
            
            start, end = num_range[num]                        
                
        
        min_range = float('inf')
        for a, b in num_range.values():
            min_range = min(b - a + 1, min_range)
            
        return min_range
                
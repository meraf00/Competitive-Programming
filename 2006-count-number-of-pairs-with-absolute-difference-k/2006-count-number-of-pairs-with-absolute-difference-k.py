class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        
        res = 0
        
        for num in nums:
            res += count[num + k]
            res += count[num - k]
            
            count[num] += 1 
            
        return res
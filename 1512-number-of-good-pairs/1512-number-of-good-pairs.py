class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        
        pairs = 0
        for freq in num_count.values():
            if freq > 1:
                pairs += freq * (freq - 1) // 2
        
        return pairs
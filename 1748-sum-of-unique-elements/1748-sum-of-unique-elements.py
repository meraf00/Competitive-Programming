class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        total = 0
        for num, num_freq in freq.items():
            if num_freq == 1:
                total += num
        
        return total
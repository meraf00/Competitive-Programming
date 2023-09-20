class Solution:
    def averageValue(self, nums: List[int]) -> int:
        mean = 0
        count = 0
        
        for num in nums:
            if num % 6 == 0:
                mean  += num
                count += 1
        
        if count == 0:
            return 0
        
        return mean // count
        
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_to_int = list(map(int, nums))
        nums_to_int.sort()
        
        return str(nums_to_int[-k])
from typing import List

class ConcatCompare(int):
    def __lt__(n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
        
class Solution:    
        
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=ConcatCompare)
        return "".join(map(str, nums))
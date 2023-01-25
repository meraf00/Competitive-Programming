class Int(int):
    def __init__(self, num):
        int().__init__(self, num)
    
    def __lt__(self, other):
        return self.compare(self, other) == -1
    
    def __gt__(self, other):
        return self.compare(self, other) == 1
    
    def compare(self, num1, num2):
        num1_str = list(str(num1))
        num2_str = list(str(num2))
        
        a = "".join(num1_str + num2_str)
        b = "".join(num2_str + num1_str)
        
        if a <= b:
            return  -1
        return 1
        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:        
        nums = list(map(Int, nums))
        nums.sort(reverse=True)
        
        nums = map(str, nums)
        
        result = "".join(nums)
        
        # remove unnecessary preceding 0's
        result = str(int(result))
        
        return result
        
        
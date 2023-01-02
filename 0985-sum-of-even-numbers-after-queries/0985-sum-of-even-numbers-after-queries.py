class Solution:
    def isEven(self, num: int) -> bool:
        if abs(num) % 2 == 0:
            return True
        return False
    
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:        
        even_sum = 0
        
        for num in nums:
            if self.isEven(num):
                even_sum += num
        
        output = []
        
        for val, index in queries:
            num = nums[index]
            
            if self.isEven(num) and self.isEven(val):
                even_sum += val
            elif not self.isEven(num) and not self.isEven(val):
                even_sum += num + val
            
            elif self.isEven(num) and not self.isEven(val):
                even_sum -= num               
            
            output.append(even_sum)                
            
            nums[index] += val                
            
        return output
            
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf
        
        for n in nums:
            if n == first_max or n == second_max or n == third_max:
                continue
                
            if n > first_max:
                third_max = second_max
                second_max = first_max
                first_max = n
            
            elif n > second_max:
                third_max = second_max
                second_max = n
            
            elif n > third_max:
                third_max = n
        
        return first_max if third_max == -inf else third_max
                
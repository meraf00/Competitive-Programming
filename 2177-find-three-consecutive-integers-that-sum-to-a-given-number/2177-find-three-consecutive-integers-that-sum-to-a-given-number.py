class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 == 0:
            first_num = (num - 3) // 3
            second_num =  first_num + 1
            third_num =  second_num + 1
            
            return [first_num, second_num, third_num]
        
        return []
        
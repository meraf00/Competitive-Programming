class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b_square = c - a ** 2
            b = sqrt(b_square)
            
            if int(b) == b:
                return True
        return False
            
        
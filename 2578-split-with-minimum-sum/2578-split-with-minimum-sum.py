class Solution:
    def splitNum(self, num: int) -> int:
        pairs = [[], []]
        
        num = list(str(num))
        num.sort()
        
        for idx, digit in enumerate(num):
            pairs[idx % 2].append(digit)
        
        num1 = ''.join(pairs[0])
        num2 = ''.join(pairs[1])
        
        return int(num1) + int(num2)
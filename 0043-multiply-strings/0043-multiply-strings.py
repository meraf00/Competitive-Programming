class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        
        value = 0
        for i, d in enumerate(reversed(num1)):
            for j, d2 in enumerate(reversed(num2)):
                n1 = int(d) * 10 ** i
                n2 = int(d2) * 10 ** j
                value += n1 * n2
        return str(value)
        
        
        
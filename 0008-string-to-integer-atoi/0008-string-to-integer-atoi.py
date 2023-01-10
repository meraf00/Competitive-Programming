class Solution:
    def myAtoi(self, s: str) -> int:
        
        pointer = 0
        
        # move pointer until the first non white space
        while pointer < len(s) and s[pointer] == " ":
            pointer += 1
            
        if pointer == len(s):
            return 0
        
        if s[pointer] == "+":
            sign = 1
            pointer += 1
            
        elif s[pointer] == "-":
            sign = -1
            pointer += 1
        
        else:
            sign = 1
        
        number = 0        
        while pointer < len(s):
            if not s[pointer].isdigit():
                break
            
            number *= 10
            number += int(s[pointer])
            pointer += 1
        
        number = sign * number
        
        if number > 2**31 - 1:
            return 2**31-1
        elif number < -2**31:
            return -2**31
        else:
            return number
            
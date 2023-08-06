class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        
        answer = []
        
        for idx, digit in enumerate(num):
            if digit == "6":
                answer.append("9")
                answer.extend(num[idx + 1:])            
                break
            
            answer.append(digit)
        
        return int("".join(answer))
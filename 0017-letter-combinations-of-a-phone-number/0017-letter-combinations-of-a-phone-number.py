class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        length = len(digits)
        
        _all_ = []
        
        current = []
        
        def backtrack(index):                        
            if len(current) == length:
                _all_.append("".join(current))                
                return
            
            if index >= length:
                return
                        
            current_digit = digits[index]            
            
            for i in range(index, length):                                
                for char in mapping[current_digit]:
                    current.append(char)                                
                    backtrack(i + 1)                
                    current.pop()                
            
            
        backtrack(0)
        
        return _all_
        
        
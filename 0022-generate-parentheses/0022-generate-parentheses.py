class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        current = []
                    
        counter = {"(": n, ")":n}
        
        def backtrack(index):                        
            if counter["("] + counter[")"] == 0:
                combinations.append("".join(current))
                return
            
            if counter["("] > counter[")"]:
                return
                                                
            for bracket in counter.keys():                
                if counter[bracket] > 0:
                    current.append(bracket) 
                    counter[bracket] -= 1

                    backtrack(index + 1)

                    counter[bracket] += 1
                    current.pop()                    
            
        
        backtrack(0)
        
        return combinations
        
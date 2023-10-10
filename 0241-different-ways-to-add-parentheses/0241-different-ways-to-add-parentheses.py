class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        exp = []
        
        left = 0
        
        n = len(expression)
        
        for right in range(n + 1):            
            if right == n:
                exp.append(int(expression[left:right]))
                break
                
            if not expression[right].isdigit():
                exp.append(int(expression[left:right]))
                exp.append(expression[right])
                left = right + 1                        
                        
        def evaluate(a, b, op):                        
            if op == '-':
                return a - b
            
            elif op == '+':
                return a + b
        
            elif op == '*':
                return a * b
        
        @cache
        def dp(i, j):  
            if i == j:
                return [exp[i]]
            
            if j - i == 2:
                return [evaluate(exp[i], exp[j], exp[i + 1])]
            
            ans = []
            
            for k in range(i, j, 2):
                op = exp[k + 1]
                
                left = dp(i, k)                
                right = dp(k + 2, j)                                
                
                for a in left:
                    for b in right:                
                        ans.append(evaluate(a, b, op))
            
            return ans
                        
        return dp(0, len(exp) - 1)
        
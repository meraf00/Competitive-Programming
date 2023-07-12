class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_before_j = [float('-inf')]
        
        answer = float('-inf')
        
        for j, vj in enumerate(values):
            last_max = max_before_j[-1]
            
            max_before_j.append(max(last_max, j + vj))
            
            answer = max(answer, max_before_j[-2] + vj - j)
        
                                
        return answer
        
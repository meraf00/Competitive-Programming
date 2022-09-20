"""
https://leetcode.com/problems/solving-questions-with-brainpower/
"""

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cummulative_points = [0] * len(questions)
        
        for i in range(len(questions)-1, -1, -1):
            pts, bp = questions[i]
            
            # if question[i] is done
            if i + bp + 1 < len(questions):
                cummulative_points[i] = cummulative_points[i + bp + 1]         
                
            cummulative_points[i] += pts
                        
            if i + 1 < len(questions):
                # max between doing and not doing quesition
                cummulative_points[i] = max(cummulative_points[i+1], cummulative_points[i]) 
                
        return max(cummulative_points)
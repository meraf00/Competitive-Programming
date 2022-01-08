from typing import List

class Solution:            
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:       
        
        expanded = []
        for i in intervals:            
            for j in range(i[0], i[1]):
                if j not in expanded:
                    expanded.append(j)
        
        expanded.sort()
        
        answer = []
        for i in intervals:            
            if (i[0] == i[1]) and (i[0] not in expanded and i[0] - 1 not in expanded and i not in answer):
                answer.append(i)
        
        if expanded:
            begin = expanded[0]
            for i in range(len(expanded) - 1):
                if expanded[i + 1] - expanded[i] != 1:
                    answer.append([begin, expanded[i] + 1])
                    begin = expanded[i + 1]

            answer.append([begin, expanded[-1] + 1])

        answer.sort()
        
        return answer

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        
        n_first = len(firstList)
        n_second = len(secondList)
        
        ans = []
        while first < n_first and second < n_second:
            fs, fe = firstList[first]
            ss, se = secondList[second]
            
            if fs <= ss <= fe or fs <= se <= fe or \
                ss <= fs <= se or ss <= fe <= se:
                    int_start = max(fs, ss)
                    int_end = min(fe, se)
                    
                    ans.append((int_start, int_end))
                    
                                           
            if se > fe:
                first += 1

            elif fe > se:
                second += 1

            else:
                first += 1
                second += 1             
        
        return ans
                    
                
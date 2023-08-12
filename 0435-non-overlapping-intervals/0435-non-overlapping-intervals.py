class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time        
        intervals.sort(key = lambda x: x[-1])
        
        removed_count = 0
                
        previous_idx = 0
        
        for curr_idx in range(1, len(intervals)):
            prev_end = intervals[previous_idx][1]
            
            current_start = intervals[curr_idx][0]
            
            if current_start < prev_end:
                removed_count += 1
                continue
            
            previous_idx = curr_idx
        
        return removed_count
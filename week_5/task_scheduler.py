"""
https://leetcode.com/problems/task-scheduler/
"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:                
        
        counter = {}
        
        for task in tasks:
            if counter.get(task):
                counter[task] += 1
            else:
                counter[task] = 1       
        
        max_freq = max(counter.values())
        tasks_with_max_freq = 0
        for freq in counter.values():
            if freq == max_freq:
                tasks_with_max_freq += 1
        
        return max(len(tasks), (max_freq - 1) * (n + 1) + tasks_with_max_freq)
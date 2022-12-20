class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = float("inf")
        max_ = float("-inf")
        sum_ = 0
        for s in salary:
            min_ = min(s, min_)
            max_ = max(s, max_)
            sum_ += s
        
        return (sum_ - min_ - max_) / (len(salary) - 2)
        
        
        
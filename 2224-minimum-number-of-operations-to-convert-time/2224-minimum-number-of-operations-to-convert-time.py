class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_str_hour, current_str_minute = current.split(':')
        correct_str_hour, correct_str_minute = correct.split(':')
        
        current_hour = int(current_str_hour)
        current_minute = int(current_str_minute)
        
        correct_hour = int(correct_str_hour)
        correct_minute = int(correct_str_minute)
        
        current = current_hour * 60 + current_minute
        correct = correct_hour * 60 + correct_minute
        
        diff = correct - current
        
        operations = 0
        
        options = [60, 15, 5, 1]
        
        idx = 0
        
        while diff > 0:
            if diff < options[idx]:
                idx += 1
                continue
            
            diff -= options[idx]
            operations += 1
        
        return operations
            
        
        
        
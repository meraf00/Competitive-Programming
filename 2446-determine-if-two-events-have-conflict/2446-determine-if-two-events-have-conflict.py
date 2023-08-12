class Solution:
    def convert_to_seconds(self, hh_mm_format: str) -> int:
        hours, minutes = hh_mm_format.split(':')
        
        hours = int(hours)
        minutes = int(minutes)
        
        seconds = hours * 3600 + minutes * 60
        
        return seconds
        
    
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:        
        start_1, end_1 = map(self.convert_to_seconds, event1)
        start_2, end_2 = map(self.convert_to_seconds, event2)
        
        if start_1 <= start_2 <= end_1 or start_1 <= end_2 <= end_1 or start_2 <= start_1 <= end_2 or start_2 <= end_1 <= end_2:
            return True
        
        return False
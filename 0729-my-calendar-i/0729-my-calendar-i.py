class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_right(self.events, (start, end))        
        
        if not self.events:
            self.events.append((start, end))
            return True
        
        elif idx > 0 and self.events[idx - 1][1] > start:
            return False
        
        elif idx < len(self.events) and self.events[idx][0] < end:
            return False
        
        else:
            self.events.append((start, end))
            self.events.sort()
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
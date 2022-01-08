class RecentCounter:

    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:        
        self.queue.append(t)
        
        while self.queue and t - 3000 > self.queue[0]:
            del self.queue[0]
        
        return len(self.queue)

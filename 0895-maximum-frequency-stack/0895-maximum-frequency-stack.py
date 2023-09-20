class FreqStack:

    def __init__(self):
        self.heap = []
        self.freq = defaultdict(int)
        self.current_idx = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        
        v = (-self.freq[val], -self.current_idx, val)
        
        self.current_idx += 1
        
        heappush(self.heap, v)        

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.freq[val] -= 1        
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
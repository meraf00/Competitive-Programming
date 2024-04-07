class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:  
        while self.i < len(self.encoding) and self.encoding[self.i] <= 0:
            self.i += 2 

        if self.i >= len(self.encoding):
            return -1
        
        if n <= self.encoding[self.i]:
            self.encoding[self.i] -= n
            return self.encoding[self.i + 1]
        
        else:       
            moves = self.encoding[self.i]
            self.i += 2
            return self.next(n - moves)
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
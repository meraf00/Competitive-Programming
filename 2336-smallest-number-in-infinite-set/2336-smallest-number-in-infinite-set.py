class SmallestInfiniteSet:

    def __init__(self):        
        self.exist = [True for i in range(1, 1001)]
        self.smallest_idx = 0

    def popSmallest(self) -> int:
        while not self.exist[self.smallest_idx]:
            self.smallest_idx += 1
        
        self.exist[self.smallest_idx] = False
        return self.smallest_idx + 1
        

    def addBack(self, num: int) -> None:        
        self.smallest_idx = min(self.smallest_idx, num - 1)
        self.exist[num - 1] = True
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
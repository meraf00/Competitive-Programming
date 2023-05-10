class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:        
        heappush(self.right, num)
        val = heappop(self.right)
        heappush(self.left, -val)
        
        if len(self.right) < len(self.left):
            val = heappop(self.left)
            heappush(self.right, -val)
        
        
    def findMedian(self) -> float:                   
        if len(self.left) != len(self.right):
            return self.right[0]
        return (-self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
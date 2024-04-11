class LUPrefix:

    def __init__(self, n: int):
        self.prefix = 0
        self.right = []
        

    def upload(self, video: int) -> None:
        if video < self.prefix:
            return
        
        heappush(self.right, video)
        
        while self.right and self.right[0] <= self.prefix + 1:
            self.prefix = heappop(self.right)
            

    def longest(self) -> int:
        return self.prefix
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
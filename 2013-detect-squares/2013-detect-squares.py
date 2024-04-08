class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.max_x = 0
        self.max_y = 0

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.max_x = max(point[0], self.max_x)
        self.max_y = max(point[1], self.max_y)
                        
    def count(self, point: List[int]) -> int:
        x, y = point
        
        if x > self.max_x or y > self.max_y:
            return 0
        
        max_side = max(abs(self.max_x - x), abs(self.max_y - y), x, y)        
        
        count = 0
        
        for s in range(1, max_side + 1):
            count += self.points[(x + s, y)] * self.points[(x + s, y + s)] * self.points[(x, y + s)]
            count += self.points[(x + s, y)] * self.points[(x + s, y - s)] * self.points[(x, y - s)]
            count += self.points[(x - s, y)] * self.points[(x - s, y - s)] * self.points[(x, y - s)]
            count += self.points[(x - s, y)] * self.points[(x - s, y + s)] * self.points[(x, y + s)]
                               
        return count
            
            
                
            
            
            
            
            
            
        
        
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
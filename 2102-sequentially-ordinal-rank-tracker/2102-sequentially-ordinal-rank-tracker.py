class CityScore:
    def __init__(self, score, name):
        self.score = score
        self.name = name
        self.parity = 1
        
    def __neg__(self):        
        neg = CityScore(self.score, self.name)
        neg.parity = self.parity * -1
        
        return neg
        
    
    def __lt__(self, other):
        if self.parity != other.parity:
            return self.parity < other.parity
        
        if self.parity == 1:
            if self.score < other.score:
                return True

            elif self.score > other.score:
                return False

            else:
                return self.name > other.name
        
        else:
            if -self.score < -other.score:
                return True

            elif -self.score > -other.score:
                return False

            else:
                return self.name < other.name
                

    def __str__(self):
        return f'{(self.parity * self.score, self.name)}'
    
    def __repr__(self):
        return f'{(self.parity * self.score, self.name)}'
        

class SORTracker:

    def __init__(self):
        self.left = []
        self.right = []  
        self.query_count = 0    

    def add(self, name: str, score: int) -> None:
        city_score = CityScore(score, name)
        
        heappush(self.right, -city_score)
        
        while self.left:            
            right_city = heappop(self.right)
            left_city = heappop(self.left)
            
            if -right_city > left_city:
                heappush(self.right, -left_city)
                heappush(self.left, -right_city)
                
            else:
                heappush(self.right, right_city)
                heappush(self.left, left_city)
                break
        
        while len(self.left) < self.query_count:
            right_city = heappop(self.right)
            heappush(self.left, -right_city)                
        
    def get(self) -> str:  
        self.query_count += 1
        
        while len(self.left) < self.query_count:
            right_city = heappop(self.right)
            heappush(self.left, -right_city)
        
        
        return self.left[0].name
        
        
        
        
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
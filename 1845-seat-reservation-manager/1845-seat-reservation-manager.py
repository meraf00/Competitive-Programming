class SeatManager:

    def __init__(self, n: int):
        self.unreserved_seats = []
        self.is_unreserved = set()   
        self.current = 1

    def reserve(self) -> int:
        if self.unreserved_seats:
            answer = heappop(self.unreserved_seats)
            self.is_unreserved.remove(answer)
            
        else:
            answer = self.current
            self.current += 1
        
        return answer
        

    def unreserve(self, seatNumber: int) -> None:
        if self.current <= seatNumber or seatNumber in self.is_unreserved:
            return
        
        self.is_unreserved.add(seatNumber)
        
        heappush(self.unreserved_seats, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
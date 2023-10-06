class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()        
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        
        # print(self.front, self.back, f'push front {val}')

    def pushMiddle(self, val: int) -> None:
        if len(self.front) == len(self.back):
            self.front.append(val)

            if len(self.front) > len(self.back) + 1:
                self.back.appendleft(self.front.pop())
        
        else:
            self.back.appendleft(self.front.pop())            
            self.front.append(val)
        
        # print(self.front, self.back, f'push middle {val}')

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        
        if len(self.back) > len(self.front):
            self.front.append(self.back.popleft())
        
        # print(self.front, self.back, f'push back {val}')

    def popFront(self) -> int:
        if not self.front:
            return -1
        
        val = self.front.popleft()
        
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        
        # print(self.front, self.back, f'pop front {val}')
        
        return val

    def popMiddle(self) -> int:
        if not self.front:
            return -1
        
        val = self.front.pop()
        
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        
        # print(self.front, self.back, f'pop middle {val}')
        
        return val
        

    def popBack(self) -> int:
        if not self.front:
            return -1
        
        if not self.back:
            return self.front.pop()
        
        val = self.back.pop()
        
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        
        # print(self.front, self.back, f'pop back {val}')
        
        return val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
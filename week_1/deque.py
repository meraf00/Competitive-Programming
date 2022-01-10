class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque = [value] + self.deque
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.deque:
            del self.deque[0]
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque:
            del self.deque[-1]
            return True
        return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        return -1
    
    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        return False

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        new = Node(url, self.current)
        self.current.next = new
        self.current = new        
        
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current == self.homepage:
                break
                
            self.current = self.current.prev
        
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.next:
                break
                
            self.current = self.current.next
        
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
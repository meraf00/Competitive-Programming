class Solution:
    def gcd(self, a, b):
        if b:
            return gcd(b, a % b)
        return a
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        
        if reduce(self.gcd, counter.values()) != 1:
            return True
        
        return False
        
        
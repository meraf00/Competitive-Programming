class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n % 3 == 0:        
            return self.isPowerOfThree(n // 3)
        
        return False
            

if __name__ == "__main__":
    s = Solution()
    a = 27, 9, 27, 0, 1, 54, 0, 999999
    for i in a:
        print("I =", i)
        r = s.isPowerOfThree(i)
        print(r)
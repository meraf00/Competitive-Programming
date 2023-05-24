class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        
        nums = [(numOnes, 1), (numZeros, 0), (numNegOnes, -1)]
        
        for n, value in nums:
            if k == 0:
                break
                
            if n <= k:
                total += value * n
                k -= n
            
            else:
                total += k * value
                break
        
        return total
        
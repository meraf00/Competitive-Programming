class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        
        op = 0
        
        for n in nums:
            if n > k:
                continue
                
            if count.get(k-n):
                count[k-n] -= 1
                op += 1
            else:
                if count.get(n):
                    count[n] += 1
                else:
                    count[n] = 1
        return op
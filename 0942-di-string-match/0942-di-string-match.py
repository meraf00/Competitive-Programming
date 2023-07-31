class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = [0] * (len(s) + 1)
        
        largest = len(s)
        smallest = 0
        
        for i in range(len(s), -1, -1):
            if s[i - 1] == "I":
                perm[i] = largest
                largest -= 1
            
            else:
                perm[i] = smallest
                smallest += 1
        
        return perm        
                
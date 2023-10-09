class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26

        freq2 = [0] * 26
        
        for char in s1:
            asci = ord(char) - ord('a')
            freq1[asci] += 1

        for right in range(len(s1)):
            asci = ord(s2[right]) - ord('a')
            freq2[asci] += 1
            
        if freq1 == freq2:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            asci_r = ord(s2[right]) - ord('a')            
            asci_l = ord(s2[left]) - ord('a')            
            
            freq2[asci_r] += 1
            freq2[asci_l] -= 1
            
            if freq1 == freq2:
                return True
        
            left += 1
        
        return False
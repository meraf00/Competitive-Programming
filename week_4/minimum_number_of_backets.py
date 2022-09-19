"""
https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
"""

class Solution:
    def minimumBuckets(self, street: str) -> int:
        if len(street) > 1 and street[0] == street[1] == "H":
            return -1
        
        if len(street) > 1 and street[-1] == street[-2] == "H":
            return -1
        
        if len(street) == 1:
            return -1 if street[0] == "H" else 0
            
        street = list(street)
        for i, c in enumerate(street):
            if c == "H":                
                if i + 1 < len(street) and street[i+1] == ".":
                    if i-1 > -1 and street[i-1] != "B":
                        street[i+1] = "B"
                    elif i == 0:
                        street[i + 1] = "B"
                elif i - 1 > -1 and street[i - 1] == ".":
                    street[i-1] = "B"
                elif i + 1 < len(street) and i - 1 > -1 and street[i+1] == street[i-1] == "H":
                    return -1
        
        buckets = 0
        for c in street:
            if c == "B":
                buckets += 1
        return buckets
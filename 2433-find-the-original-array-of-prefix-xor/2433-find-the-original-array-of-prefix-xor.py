class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        
        for i in range(1, len(pref)):
            answer.append(pref[i - 1] ^ pref[i])
        
        return answer
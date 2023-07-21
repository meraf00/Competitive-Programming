class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:        
        length = len(answerKey)
        
        counter = {
            "T": 0,
            "F": 0
        } 
        
        left = 0
        max_confussion = 0
        
        for answer in answerKey:
            counter[answer] += 1
                
            while counter['T'] > k and counter['F'] > k:
                ans = answerKey[left]
                counter[ans] -= 1
                left += 1
            
            max_confussion = max(max_confussion, counter['T'] + counter['F'])
            
        return max_confussion
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_counter = defaultdict(int)
        
        answer = []
        
        left = 0        
        for right in range(9, len(s)):              
            sequence = s[left:right+1] 
            
            left += 1
            
            # greater than one means already inside answer
            if seq_counter[sequence] == 1:
                answer.append(sequence)
            
            seq_counter[sequence] += 1

        return answer
            
        
        
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        note_counter = defaultdict(int)
        
        for count, bill in enumerate(bills):
            note_counter[bill] += 1
            
            if bill == 10:
                if note_counter[5]:
                    note_counter[5] -= 1
                else:
                    return False
            
            elif bill == 20:
                if note_counter[10] and note_counter[5]:
                    note_counter[5] -= 1
                    note_counter[10] -= 1                    
                
                elif note_counter[5] >= 3:
                    note_counter[5] -= 3
                
                else:
                    return False
            
        return True
                    
                
                    
                
            
                
                    
                    
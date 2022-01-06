from typing import List

class Solution:
    
    def gradingStudents(self, grades: List[int]) -> List[int]:
        
        output = []
        
        for grade in grades:
            if grade > 37 and (grade % 5) >= 3:
                output.append ( grade + (5 - (grade % 5)) )
            else:
                output.append ( grade )
            
        return output

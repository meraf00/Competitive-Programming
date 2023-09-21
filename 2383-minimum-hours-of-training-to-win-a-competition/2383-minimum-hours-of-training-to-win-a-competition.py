class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:                
                        
        total_energy_req = sum(energy)
        
        training_hours = max(total_energy_req - initialEnergy + 1, 0)
                
        curr_xp = initialExperience
                
        for xp in experience:
            print(curr_xp)
            if curr_xp <= xp:
                training_hours += xp - curr_xp + 1
                curr_xp = xp + 1
            
            curr_xp += xp
            
            
            
        return training_hours          

    
"""
5
1
[1,4,3,2, 50]
[2,6,3,1, 1]
11
23
[69,22,93,68,57,76,54,72,8,78,88,15,58,61,25,70,58,91,79,22,91,74,90,75,31,53,31,7,51,96,76,17,64,89,83,54,28,33,32,45,20]
[51,81,46,80,56,7,46,74,64,20,84,66,13,91,49,30,75,43,74,88,82,51,72,4,80,30,10,19,40,27,21,71,24,94,79,13,40,28,63,85,70]    
5
3
[1,4,3,2]
[2,6,3,1]
2
4
[1]
[3]
1
1
[1,1,1,1]
[1,1,1,50]
"""
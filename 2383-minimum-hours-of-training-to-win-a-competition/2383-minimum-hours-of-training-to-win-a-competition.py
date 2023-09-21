class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:                
                        
        total_energy_req = sum(energy)
        
        training_hours = max(total_energy_req - initialEnergy + 1, 0)
                
        curr_xp = initialExperience
                
        for xp in experience:            
            if curr_xp <= xp:
                training_hours += xp - curr_xp + 1
                curr_xp = xp + 1
            
            curr_xp += xp
                                    
        return training_hours          


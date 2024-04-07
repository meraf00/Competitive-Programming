class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        
        target = 0
        
        skill_idx = {}
        
        for i, skill in enumerate(req_skills):
            target |= 1 << i
            skill_idx[skill] = i
        
        @cache
        def dp(i, skills): 
            if skills == target:
                return 0
            
            if i >= n:                 
                return -1
            
            take = skills
            
            for skill in people[i]:
                if skill in skill_idx:
                    take |= 1 << skill_idx[skill]
                        
            team1 = dp(i + 1, take) | (1 << i)
            team2 = dp(i + 1, skills)
            
            
            
            if team1 == -1:
                return team2
            elif team2 == -1:
                return team1
            elif team1.bit_count() < team2.bit_count():
                return team1
            else:
                return team2
            
        
        team = dp(0, 0)                
        
        ans = []
        for i in range(n):
            if team & (1 << i):
                ans.append(i)
                
        return ans
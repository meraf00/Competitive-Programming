class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))  
        
        n_players = len(players)
        
        dp_with = [0] * (n_players + 1)        
        dp_without = [0] * (n_players + 1)
                        
        for i in range(n_players):
            curr_age, curr_score = players[i]  
            prev_score = players[i - 1][1]
                        
            for j in range(i, -1, -1):
                age, score = players[j]

                if score <= curr_score:                     
                    dp_with[i + 1] = max(dp_with[j + 1] + curr_score, dp_with[i + 1])

            dp_without[i + 1] = max(dp_with[i], dp_without[i])
          
        
        return max(dp_with[-1], dp_without[-1])

    
"""
[1,3,5,10,15]
[1,2,3,4,5]
[4,5,6,5]
[2,1,2,1]
[1,2,3,5]
[8,9,10,1]
[564,915,436,927,784,205,186,992,518,467,264,180,528,594,557,462,667,856,104,911,960,176,382,96,153,685,359,370,623,480,213,180,881,333,658,964,367,261,758,822,790,904,246,441,97,938,202,434,88,24,881,147,439,260,47,27,39,79,751,758,493,950,94,224,769]
[6,92,61,16,66,19,63,57,6,29,17,30,67,57,89,88,4,78,29,36,18,17,41,70,5,52,4,71,35,57,46,85,21,45,58,54,45,58,93,67,59,25,58,11,95,79,94,81,85,50,29,93,3,29,21,27,6,70,24,58,96,65,4,49,73]
"""
            
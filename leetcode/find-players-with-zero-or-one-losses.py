class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)
        
        players = set()
        
        for winner, loser in matches:
            loss_count[loser] += 1
            players.add(winner)
            players.add(loser)
        
        
        answer = [[], []]
        
        for player in players:
            if loss_count[player] == 0:
                answer[0].append(player)
                
            if loss_count[player] == 1:
                answer[1].append(player)
                
        answer[0].sort()
        answer[1].sort()
        
        return answer
            
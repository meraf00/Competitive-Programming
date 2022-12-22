class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counter = {}
        
        for winner, loser in matches:
            if not loss_counter.get(winner):                
                loss_counter[winner] = 0
            
            if loss_counter.get(loser):
                loss_counter[loser] += 1
                
            else:
                loss_counter[loser] = 1
        
        output = [[], []]
        for player, loss in loss_counter.items():
            if loss == 0:
                output[0].append(player)
            elif loss == 1:
                output[1].append(player)
        
        output[0].sort()
        output[1].sort()
        
        return output
                
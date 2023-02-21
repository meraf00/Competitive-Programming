class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player_index = 0
        trainer_index = 0
        
        match_count = 0
        while trainer_index < len(trainers) and player_index < len(players):
            player_skill = players[player_index]
            trainer_skill = trainers[trainer_index]
            
            if player_skill <= trainer_skill:
                player_index += 1
                trainer_index += 1
                match_count += 1
            
            else:
                trainer_index += 1
        
        return match_count
            
        
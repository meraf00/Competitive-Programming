def count_teams(players, target):
    players.sort()

    left  = 0
    right = len(players) - 1
    count = 0
    
    team_size = 2

    while left < right:
        if players[left] >= target:
            count += 1
            left += 1
        
        elif players[right] >= target:
            right -= 1
            count += 1
        
        elif players[right] * team_size >= target:
            left += 1
            right -= 1
            count += 1
            team_size = 2
        
        else:
            team_size += 1
            left += 1
    
    return count
        



teams, enemy_power = map(int, input().split())

players = list(map(int, input().split()))

print(count_teams(players, enemy_power))
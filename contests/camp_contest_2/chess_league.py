def find_winner(player1, player2, k):        
    if abs(ratings[player1] - ratings[player2]) > k:
        return [player1 if ratings[player1] > ratings[player2] else player2]
    return [player1, player2]

def group(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i:i+2])
    
    return result

def match(group1, group2, k):
    possible_winners = set()
    for player1 in group1:
        for player2 in group2:            
            temp = find_winner(player1, player2, k)
            if len(temp) == 1:
                if temp[0] == player1:
                    possible_winners.discard(player2)
                else:
                    possible_winners.discard(player1)
                possible_winners.add(temp[0])
            else:
                possible_winners.add(player1)
                possible_winners.add(player2)
            
    return list(possible_winners)

def solve(grouped, rounds, k):
    if len(grouped) == 1:
        return grouped
        
    after_match = []
    for i in range(0, len(grouped) - 1, 2):
        after_match.append(match(grouped[i], grouped[i +1], k))
        
    return solve(after_match, rounds - 1, k)



def first_round(ratings, k):    
    
    grouped = group(list(range(len(ratings))))
    possible_winners = set()
    after_match = []
    
    for player1, player2 in grouped:
        first_round = find_winner(player1, player2, k)

        if len(first_round) == 1:
            if first_round[0] == player1:
                possible_winners.discard(player2)
            else:
                possible_winners.discard(player1)
            possible_winners.add(first_round[0])
        else:
            possible_winners.add(player1)
            possible_winners.add(player2)
        
        after_match.append(first_round)
    
    return after_match



n, k = map(int, input().split())

ratings = list(map(int, input().split()))

# print(*group(ratings, k))
# print(*first_round(ratings, k))
# print(solve(first_round(ratings, k), 1, k))
print(*sorted(map(lambda x: x+1, *solve(first_round(ratings, k), 1, k))))
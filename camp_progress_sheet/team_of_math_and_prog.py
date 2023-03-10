# https://codeforces.com/problemset/problem/1611/B

test_cases = int(input())

for _ in range(test_cases):
    prog, math = map(int, input().split())

    team_count = 0

    while prog > 0 and math > 0 and prog + math >= 4:
        if prog > math:
            prog -= 3
            math -= 1            
        
        elif prog < math:
            prog -= 1
            math -= 3
        
        else:
            team_count += prog // 2
            break

        team_count += 1
    
    print(team_count)
# https://codeforces.com/problemset/problem/1611/B


def is_feasible(prog, math, teams):
    if min(prog, math) < teams:
        return False
    
    # assign 1 prog and 1 math for each team
    remaining_prog = prog - teams
    remaining_math = math - teams

    
    # distribute the rest among the teams
    return (remaining_prog + remaining_math) / 2 >= teams



def form_max_possible_groups(prog, math):
    low = 0
    high = (prog + math) // 4

    
    while low <= high:
        mid = low + (high - low) // 2

        # can't form that much group, decrease teams
        if is_feasible(prog, math, mid):
            low = mid + 1
        
        else:
            high = mid - 1
    
    return high




test_cases = int(input())


for _ in range(test_cases):
    programmers, mathematicians = map(int, input().split())

    print(form_max_possible_groups(programmers, mathematicians))
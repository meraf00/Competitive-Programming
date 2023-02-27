test_cases = int(input())


def revive(soldiers, iters):
    length = len(soldiers)
    
    soldiers.append(0)

    for j in range(iters):
        new = [s for s in soldiers]
        for i in range(length):        
            if soldiers[i-1] == 1 and soldiers[i+1] == 1:
                continue
            
            if soldiers[i-1] == 1 or soldiers[i+1] == 1:
                new[i] = 1                                      
        
        if new == soldiers:
            break
        soldiers = new

    return "".join(map(str, soldiers[:-1]))


for _ in range(test_cases):
    n_soldiers, iters = map(int, input().split())
    soldiers = list(map(int, input()))

    print(revive(soldiers, iters))



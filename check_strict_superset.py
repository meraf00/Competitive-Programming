# Enter your code here. Read input from STDIN. Print output to STDOUT

def isSuperSet(A, sets):    
    A = set(A)
    sets_union = set()
    
    # check if all items are in A
    for set_ in sets:
        for item in set_:
            if item not in A:
                return False
    
    # check if A has atleast one more item than the rest union
    if len(A) > len(sets_union):
        return True

    return False
    

    
if __name__ == "__main__":
    # take input
    
    first_line = input().split()
    first_line = map(int, first_line)
    A = list(first_line)
    
    n = int(input())
    sets = []
    
    for _ in range(n):
        line = input().split()
        line = map(int, line)  
        line = list(line)      
        sets.append(line)
    
    print(isSuperSet(A, sets))
    
    
    
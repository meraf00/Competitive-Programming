test_cases = int(input())


for _ in range(test_cases):
    string = input() + " "
    
    left = 0
    for right in range(len(string)):
        if string[right] != string[left]:
            length = right - left
            left  = right
            if length == 1:
                print("NO")
                break
            
    else:
        print("YES")

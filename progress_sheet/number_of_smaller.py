# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

len_1, len_2 = map(int, input().split())
array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

pointer_1 = 0
pointer_2 = 0

answer = [0] * len(array_2)

while pointer_1 < len_1 and pointer_2 < len_2:
    
    num_1 = array_1[pointer_1]
    num_2 = array_2[pointer_2]
    
    if num_1 < num_2:
        pointer_1 += 1        
    else:
        array_2[pointer_2] = pointer_1
        pointer_2 += 1

while pointer_2 < len_2:
    array_2[pointer_2] = pointer_1
    pointer_2 += 1


print(*array_2)

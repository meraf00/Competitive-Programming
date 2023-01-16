"""https://codeforces.com/gym/421441/problem/B"""

array_size = int(input())
array = list(map(int, input().split()))

counter = {"-":[], "+":[], 0: []}
for element in array:
    if element < 0:
        counter['-'].append(str(element))
    elif element > 0:
        counter['+'].append(str(element))
    else:
        counter[0].append(str(element))
    
num_of_negatives = len(counter["-"])
num_of_positives = len(counter["+"])
num_of_zeros = len(counter[0])

if num_of_positives == 0:
    counter["+"].extend(counter["-"][-2:])
    counter["-"] = counter["-"][:-2]
    num_of_negatives = len(counter["-"])
    num_of_positives = len(counter["+"])
    num_of_zeros = len(counter[0])

if num_of_negatives % 2 == 0 :
    print(num_of_negatives - 1, " ".join(counter["-"][:-1]))
    print(num_of_positives, " ".join(counter["+"]))
    print(num_of_zeros + 1, " ".join(counter[0] + [counter["-"][-1]]))

else:
    print(num_of_negatives, " ".join(counter["-"]))
    print(num_of_positives, " ".join(counter["+"]))
    print(num_of_zeros, " ".join(counter[0]))




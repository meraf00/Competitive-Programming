from collections import *
import string
import sys

n = int(input())

words = []

for _ in range(n):
    words.append(input())


graph = defaultdict(list)
degree = defaultdict(int)

all_letters = set()
for i in range(n - 1):
    first_word = words[i]
    second_word = words[i + 1]

    all_letters.update(first_word)
    all_letters.update(second_word)    

    for a, b in zip(first_word, second_word):  
        
        if a != b:
            graph[a].append(b)
            degree[b] += 1
            break
    
    else:
        if len(first_word) > len(second_word):
            print("Impossible")
            sys.exit()
    
queue = deque()
for letter in all_letters:
    if degree[letter] == 0:
        queue.append(letter)
        degree[letter] -= 1


order = []

while queue:
    current = queue.popleft()

    order.append(current)

    for nbr in graph[current]:
        degree[nbr] -= 1

        if degree[nbr] == 0:
            queue.append(nbr)


if len(order) == len(all_letters):
    letters = set(string.ascii_lowercase)
    other = letters - set(order)

    actual_order = list(other) + order

    print(*actual_order, sep="")

else:
    print("Impossible")

